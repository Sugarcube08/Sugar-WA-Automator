import os
import traceback
import pickle
import random
from shutil import which    
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def banner():
    print(r"""
███████╗██╗   ██╗ ██████╗  █████╗ ██████╗      ██     ██  █████╗    
██╔════╝██║   ██║██╔════╝ ██╔══██╗██╔══██╗     ██     ██ ██   ██        
███████╗██║   ██║██║  ███╗███████║██████╔╝     ██  █  ██ ███████    
╚════██║██║   ██║██║   ██║██╔══██║██║  ██║     ██ ███ ██ ██   ██    
███████║╚██████╔╝╚██████╔╝██║  ██║██║  ██║      ███ ███  ██   ██    
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝      ╚══ ╚═╝  ╚═╝  ╚═╝                             
🚀 Sugar WA Automator 🚀
⚡ Bulk WhatsApp Messaging Tool ⚡
-------------------------------------
📩 Automate WhatsApp messages with ease!
📂 Supports file-based and auto-generated contacts
🛠️ Uses Selenium for web automation
🔒 Secure and efficient
-------------------------------------

---

Made with ❤️  by SugarCube
---
Support Me
If you find this project helpful, consider buying me a coffee!
---

""")


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
    chrome_path = which("chromium-browser")
    if not chrome_path:
        raise Exception("Chromium browser is not available.")
    chrome_options.binary_location = chrome_path
    
    chrome_options.add_argument("--start-minimized")  # Start minimized instead of maximized
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (useful in Linux)
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevents /dev/shm errors in Docker
    chrome_options.add_argument("--disable-gpu")  # Disables GPU acceleration (required in headless)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Reduces bot detection
    chrome_options.add_argument("--disable-software-rasterizer")  # No software-based GPU rendering
    chrome_options.add_argument("--window-size=1920,1080")  # Set a default resolution
    chrome_options.add_argument(f"--user-data-dir={profile_dir}")  # Use custom Chrome profile
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Hides automation banner
    chrome_options.add_experimental_option("useAutomationExtension", False)  # Disables automation extension
    chrome_options.add_argument("--disable-popup-blocking")  # Ensures popups are not blocked
    chrome_options.add_argument("--disable-features=OptimizationGuide,PaintHolding")
    chrome_options.add_argument("--disable-background-networking")  # Disables background Chrome services
    chrome_options.add_argument("--disable-sync")  # Disables Chrome account sync
    chrome_options.add_argument("--disable-renderer-backgrounding")  # Keeps renderer active even when idle
    chrome_options.add_argument("--disable-site-isolation-trials")  # Prevents extra security measures
    chrome_options.add_argument("--disable-translate")  # Disables automatic Google Translate prompts
    chrome_options.add_argument("--metrics-recording-only")  # Reduces resource usage
    chrome_options.add_argument("--log-level=3")  # Suppresses warnings and errors in logs
    chrome_options.add_argument("--enable-automation")  # Ensures automation mode is enabled
    chrome_options.add_argument("--no-first-run")  # Skips Chrome’s first-run setup dialogs
    chrome_options.add_argument("--password-store=basic")  # Avoids credential popups
    chrome_options.add_argument("--disable-ipc-flooding-protection")  # Prevents throttling of IPC messages
    chrome_options.add_argument("--disable-client-side-phishing-detection")  # Prevents Chrome from blocking scripts
    chrome_options.add_argument(f"--user-data-dir={profile_dir}")

    print("🚀 Launching Chrome with custom profile...")
    
    chromedriver_path = which("chromedriver")
    if not chromedriver_path:
        raise Exception(chromedriver_path)
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # Open WhatsApp Web
    print("🌐 Opening WhatsApp Web...")
    driver.get("https://web.whatsapp.com")
    time.sleep(2)  # Allow some initial loadi
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
        WebDriverWait(driver, 5).until(
            EC.any_of(
                EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']")),  
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'x12lqup9') and contains(@class, 'x1o1kx08')]"))
               )
        )
        time.sleep(2)  # Wait for chat to load60
        # Check if phone number is invalid
        if driver.find_elements(By.XPATH, "//div[contains(@class, 'x12lqup9') and contains(@class, 'x1o1kx08')]"):
            print(f"❌ Error: {phone_number} is NOT registered on WhatsApp. Skipping...")
            return False  # Skip to the next number

        # If no error, proceed with sending
        print("✅ Chat loaded successfully!")
        print("📌 Locating send button...")
        send_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Send']"))
        )
        print("📤 Clicking send button in 5...")
        time.sleep(1)
        print("📤 Clicking send button in 4...")
        time.sleep(1)
        print("📤 Clicking send button in 3...")
        time.sleep(1)
        print("📤 Clicking send button in 2...")
        time.sleep(1)
        print("📤 Clicking send button in 1...")
        time.sleep(1)
        send_button.click()

        print(f"✅ Message sent successfully to {phone_number}!")
        time.sleep(random.randint(1, 9))  
        return True

    except Exception as e:
        print(f"❌ Unexpected Error with {phone_number}: {e}")
        traceback.print_exc()
        return False 

def file_mode(message_path, contact_path):
    with open(message_path, "r") as message_file:
        message = message_file.read().strip()  

    with open(contact_path
              , "r") as contacts_file:
        contacts = [line.strip() for line in contacts_file.readlines() if line.strip()]

    driver = initialize_browser()

    for phone_number in contacts:
        success = send_message(phone_number, message, driver)
        if not success:
            print(f"⚠️ Skipping {phone_number} due to an issue.")

    print("✅ All messages processed.")
    driver.quit()
    
def auto_mode(message_path):
    
    with open(message_path, "r") as message_file:
        message = message_file.read().strip() 
         
    initial = int(input("Enter Initial Number to start with (without country code +91): "))
    indent = int(input("Enter Indent of Successful Sent Messages: "))
    direct = int(input("Enter Direction \n 1. Incrementing(contact+1) \n 2. Decrementing(contact-1\n>>): "))
    DBfile = "ContactDB.txt"
    driver = initialize_browser()
    i = 0
    
    if not os.path.exists(DBfile):
        with open(DBfile, "w") as file:
            file.write("")
            
    if direct == 1:
        while i < indent:
            number = "+91" + str(initial)
            flag = send_message(number , message, driver)
            initial = initial + 1
            if flag:
                with open(DBfile, "a") as file:
                    file.write(str(number) + "\n")
                    print(f"✅ {number} is added to DB")
                    i += 1
            
    elif direct == 2:
        while i < indent:
            number = "+91" + str(initial)
            flag = send_message(number, message, driver)
            initial = initial - 1
            if flag:
                with open(DBfile, "a") as file:
                    file.write(str(number) + "\n")
                    print(f"✅ {number} is added to DB")
                    i += 1
            
    else:
        print("Invalid Input")
        driver.quit()
        return
    
    print("✅ All messages processed.")
    driver.quit()
    
def clean_DB():
    
    DBfile_path = "ContactDB.txt"  # Define file name

    # Read existing numbers and store unique ones in a set
    if os.path.exists(DBfile_path):
        with open(DBfile_path, "r") as file:
            existing_numbers = {line.strip() for line in file if line.strip()}  # Remove duplicates and empty lines
    else:
        existing_numbers = set()

    # Write back unique numbers
    with open(DBfile_path, "w") as file:
        file.write("\n".join(existing_numbers) + "\n")  # Write each number on a new line

    print("✅ DataBase Cleaned and Formated.")    
               
if __name__ == "__main__": 
    banner()
    while True: 
        message_path = input("ENTER Path to message file (messages.txt or left empty for default): ").strip() or "messages.txt"
        if not os.path.exists(message_path):
            print("❌ Invalid Path. Please try again.")
            continue
        else:
            print(f"✅ Message file >{message_path}< loaded successfully.\n")
          
     
        contact_path = input("ENTER Path to contact file (contacts.txt or left empty for default): ").strip() or "contacts.txt"
        if not os.path.exists(contact_path):
            print("❌ Invalid Path. Please try again.")
            continue
        else:
            print(f"✅ Contact file >{contact_path}< loaded successfully.\n")
       
        choice = int(input("\n📌 Choose Mode: \n 1. File Mode \n 2. Auto Mode\n>>>").strip() or 3)
        if choice == 1:
            file_mode(message_path, contact_path)
        elif choice == 2:    
            auto_mode(message_path)
            clean_DB()
        else:     
            print("Invalid Input")
        
        ch = input("\nDo you want to continue? (y/n): ").strip().lower()  or "n"
        if ch == 'n':
            print("👋 Thank you for using Sugar WA Automator. Goodbye!")
            break
        else:
            continue
            
    
