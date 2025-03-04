# 🚀 WhatsApp Bulk Messaging Bot

![WhatsApp Bot](https://img.shields.io/badge/WhatsApp%20Automation-Powered%20by%20Selenium-green?style=flat-square&logo=whatsapp)

## 📌 Introduction
📲 **Sugar-WA-Automator** automates bulk messaging via **WhatsApp Web** using **Selenium**. It supports multiple messaging modes, manages browser sessions with cookies, and mimics human-like behavior to prevent detection.

---

## 🛠️ Installation Guide

### ✅ **1. Install Essential Programs**
Ensure the following are installed on your system:
- 🖥️ **Chromium Browser**
- ⚙️ **Chromedriver** (Matching your Chromium version)
- 🐍 **Python 3.x**
- 📦 **pip (Python Package Manager)**

#### **🔹 On Ubuntu:**
```bash
sudo apt update && sudo apt install -y chromium-browser python3 python3-pip
```
🔹 **Manually Install Chromedriver**:
```bash
CHROME_VERSION=$(chromium-browser --version | grep -oP '\d+\.\d+\.\d+')
wget https://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
```

#### **🔹 On Windows (Using Chocolatey):**
```powershell
choco install chromium chromedriver python
```

### ✅ **2. Install Required Python Libraries**
Navigate to the project directory and install dependencies:
```bash
pip install -r requirements.txt
```

### ✅ **3. Clone the Repository**
```bash
git clone https://github.com/Sugarcube08/Sugar-WA-Automator.git
cd Sugar-WA-Automator
```

### ✅ **4. Login to WhatsApp Web**
Run the script to log in and save session cookies:
```bash
python3 login.py
```
📌 **Scan the QR code** displayed in the browser and press Enter once logged in.

### ✅ **5. Start the Bot**
```bash
python3 run.py
```

---

## 📜 How to Use

### 1️⃣ **Prepare Your Message & Contacts**
- ✉️ Edit `messages.txt` with your message.
- ☎️ Edit `contacts.txt`, adding one phone number per line in **international format** (`+1234567890`).

### 2️⃣ **Choose a Messaging Mode**
When you run the script, it will prompt you to select a mode:

#### 🔹 **File Mode (Predefined Contacts)**
```bash
python3 run.py
```
- Loads numbers from `contacts.txt`
- Sends messages sequentially

#### 🔹 **Auto Mode (Sequential Number Generator)**
Auto Mode automatically generates phone numbers based on a starting number.
- 📌 You must enter:
  - Initial phone number (without country code, e.g., `9876543210`)
  - Number of messages to send
  - Direction: **Incrementing (+1)** or **Decrementing (-1)**

### 3️⃣ **Monitor Execution**
📊 Keep an eye on the terminal for real-time status updates.

---

## 🔧 Features
✅ **Supports Bulk Messaging** (Predefined contacts & auto-generated numbers)  
✅ **Saves & Loads WhatsApp Web Session** (No need to scan QR code every time)  
✅ **Human-Like Delays** (To prevent detection)  
✅ **Auto Mode with Number Generation**  
✅ **Database Cleaning to Remove Duplicates**  
✅ **Error Logging & Skipping Invalid Numbers**  

---

## ⚠️ Cautions
- 🚫 **Automated messaging is against WhatsApp’s Terms of Service.** Use at your own risk.
- ⏳ Avoid sending messages too quickly to prevent detection.
- ❌ Do NOT use this script for **spam** or **unsolicited messages**.
- ✅ Ensure recipients have **opted in** to receive messages to comply with regulations.
- 🔄 WhatsApp updates may **break the script**, requiring modifications.

---

## ⚖️ Responsibilities
🚨 **Disclaimer:** The developer is NOT responsible for:
- 🚫 Bans or restrictions imposed by WhatsApp.
- ⚖️ Legal consequences from misuse.
- ❗ Unexpected script failures due to WhatsApp Web updates.

⚡ **Use this tool ethically and responsibly.**

---

## 🔐 Signing Out & Clearing Data
To ensure security & privacy:
- 🗑️ Delete session cookies manually or remove `whatsapp_cookies.pkl`.
- 🚪 Log out from **WhatsApp Web** directly to invalidate the session.

```bash
rm whatsapp_cookies.pkl
```

---

## 🔧 Troubleshooting
🔍 **Facing issues? Try these fixes:**

- 🛑 **Error: Chromedriver version mismatch**
  - Install the correct version:
    ```bash
    pip install --upgrade chromedriver-autoinstaller
    ```

- 🌐 **WhatsApp Web not loading properly?**
  - Ensure **Chromium** and **Chromedriver** are installed & up to date.

- 📩 **Bot not sending messages?**
  - Check if you're logged in (`login.py` must be run first).
  - Ensure numbers in `contacts.txt` are in correct format (`+1234567890`).

---

✅ **Enjoy Messaging!**

---

### Made with ❤️  by SugarCube

---

## ☕ Support Me
If you find this project helpful, consider buying me a coffee!  
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support%20Me-orange?style=flat-square&logo=buy-me-a-coffee)](https://www.buymeacoffee.com/sugarcube08)


