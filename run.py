import os
import pickle
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def initialize_browser():
                # Fix GTK warnings
                os.environ["NO_AT_BRIDGE"] = "1"
                os.environ["MESA_LOADER_DRIVER_OVERRIDE"] = "softpipe"

                # Define profile and cookies path
                script_dir = os.path.dirname(os.path.abspath(__file__))
                profile_dir = os.path.join(script_dir, "chrome_profile")
                cookies_file = os.path.join(script_dir, "whatsapp_cookies.pkl")

                print(f"📂 Script Directory: {script_dir}")
                print(f"📁 Using Profile: {profile_dir}")
                print(f"🍪 Cookies File: {cookies_file}")

                # Ensure profile directory exists
                if not os.path.exists(profile_dir):
                    os.makedirs(profile_dir)
                    print("✅ Created profile directory.")

                # Set up Chromium options
                chrome_options = Options()
                chrome_options.binary_location = "/usr/bin/chromium-browser"
                chrome_options.add_argument("--no-sandbox")
                chrome_options.add_argument("--disable-dev-shm-usage")
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--disable-software-rasterizer")
                chrome_options.add_argument(f"--user-data-dir={profile_dir}")

                print("🚀 Launching Chrome with custom profile...")
                service = Service("/usr/bin/chromedriver")
                driver = webdriver.Chrome(service=service, options=chrome_options)

                # Open WhatsApp Web
                print("🌐 Opening WhatsApp Web...")
                driver.get("https://web.whatsapp.com")
                time.sleep(2)  # Allow some initial loading

                # Load cookies if available
                if os.path.exists(cookies_file):
                    print("🍪 Loading cookies from file...")
                    with open(cookies_file, "rb") as file:
                        cookies = pickle.load(file)
                        for cookie in cookies:
                            driver.add_cookie(cookie)
                    print("✅ Cookies applied! Refreshing page...")
                    driver.refresh()
                    time.sleep(2)  # Wait for WhatsApp to recognize session
                return driver



def send_message(phone_number, message, driver):
    url = f"https://web.whatsapp.com/send?phone={phone_number}&text={message}"
    print(f"📩 Opening chat with {phone_number}...")

    driver.get(url)

    try:
        print("⏳ Waiting for chat or error message...")
        WebDriverWait(driver, 10).until(
            EC.any_of(
                EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']")),  
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'x12lqup9') and contains(@class, 'x1o1kx08')]"))  
            )
        )

        # Check if phone number is invalid
        if driver.find_elements(By.XPATH, "//div[contains(@class, 'x12lqup9') and contains(@class, 'x1o1kx08')]"):
            print(f"❌ Error: {phone_number} is NOT registered on WhatsApp. Skipping...")
            return False  # Skip to the next number

        # If no error, proceed with sending
        print("✅ Chat loaded successfully!")
        time.sleep(2)

        print("📌 Locating send button...")
        send_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Send']"))
        )
        print("📤 Clicking send button...")
        send_button.click()

        print(f"✅ Message sent successfully to {phone_number}!")
        time.sleep(random.randint(1, 9))  
        return True

    except Exception as e:
        print(f"❌ Unexpected Error with {phone_number}: {e}")
        return False 

               
if __name__ == "__main__":
    with open("messages.txt", "r") as message_file:
        message = message_file.read().strip()  

    with open("contacts.txt", "r") as contacts_file:
        contacts = [line.strip() for line in contacts_file.readlines() if line.strip()]

    driver = initialize_browser()

    for phone_number in contacts:
        success = send_message(phone_number, message, driver)
        if not success:
            print(f"⚠️ Skipping {phone_number} due to an issue.")

    print("✅ All messages processed.")
    driver.quit()
