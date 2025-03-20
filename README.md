# 🚀 WhatsApp Bulk Messaging Bot

![WhatsApp Bot](https://img.shields.io/badge/WhatsApp%20Automation-Powered%20by%20Selenium-green?style=flat-square&logo=whatsapp)

## 📌 Introduction
📲 **Sugar-WA-Automator** automates bulk messaging via **WhatsApp Web** using **Selenium**. This bot loads contacts from a file, manages browser sessions with cookies, and mimics human-like behavior to prevent detection.

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
sudo apt update && sudo apt install -y chromium-browser chromium-chromedriver python3 python3-pip
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
1. **Prepare Your Message & Contacts**
   - ✉️ Edit `messages.txt` with your message.
   - ☎️ Edit `contacts.txt`, adding one phone number per line (international format, e.g., `+1234567890`).

2. **Run the Scripts**
   - 🔐 **Login First**: Execute `login.py` to authenticate and save session cookies.
   - 🚀 **Run the Bot**: Execute `run.py` to send messages.
   - The script will:
     - ✅ Open WhatsApp Web
     - ✅ Load session cookies (if available)
     - ✅ Send messages sequentially
     - ✅ Log errors for invalid numbers

3. **Monitor Execution**
   - 📊 Keep an eye on the terminal output for real-time status updates.

---

## 🌟 Features  

✅ **Bulk WhatsApp Messaging** – Send messages to multiple contacts efficiently.  
✅ **Automated Contact Handling** – Load contacts from a file or generate numbers dynamically.  
✅ **Smart Error Handling** – Detects invalid numbers and skips them automatically.  
✅ **Session Persistence** – Saves and loads WhatsApp Web cookies to avoid frequent logins.  
✅ **User-Controlled Execution** – Choose between **file-based** or **auto-generated** contact modes.  
✅ **Randomized Delays** – Mimics human-like behavior to prevent detection.  
✅ **Optimized Performance** – Uses Chromium with custom configurations for stability.  
✅ **Database Cleanup** – Automatically removes duplicate contacts from logs.  
✅ **Multi-Platform Support** – Works on **Ubuntu** and **Windows** with minimal setup.  

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
  - Run:
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

## ❤️ Made with Love by SugarCube
---

## ☕ Support Me
If you find this project helpful, consider buying me a coffee!
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support%20Me-orange?style=flat-square&logo=buy-me-a-coffee)](https://www.buymeacoffee.com/Sugar-WA-Automator)
