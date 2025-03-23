import os
import pickle
import time
from shutil import which
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Define profile and cookies path
script_dir = os.path.dirname(os.path.abspath(__file__))
profile_dir = os.path.join(script_dir, "chrome_profile")
cookies_file = os.path.join(script_dir, "whatsapp_cookies.pkl")

# Remove old profile if it exists
if os.path.exists(profile_dir):
    shutil.rmtree(profile_dir)
    print("🗑️ Old profile cleared.")

# Set up Chrome options
chrome_options = Options()
chrome_path = which("chromium-browser") or which("google-chrome")
chrome_options.binary_location = chrome_path
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument(f"--user-data-dir={profile_dir}")

# Set ChromeDriver path
chromedriver_path = which("chromedriver")
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for user to log in
input("📌 Scan the QR code and press Enter after login...")

# Save cookies after login
cookies = driver.get_cookies()
with open(cookies_file, "wb") as file:
    pickle.dump(cookies, file)

print("✅ Cookies saved successfully! Exiting...")

# Close the browser
driver.quit()
