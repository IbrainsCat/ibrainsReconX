import subprocess
from datetime import datetime
import requests

def send_to_telegram(message):
    bot_token = "7522572387:AAHatso-CcYstgjUyA0ewsGH6hPlDg0Ic-8"
    chat_id = "7600608772"  # Your ID from earlier
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, data=payload)
    except:
        print("⚠️ Failed to send Telegram alert.")

def scan_target(target):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"scan_results/{target}_{timestamp}.txt"
    print(f"🛰️ Scanning {target}...\n")

    cmd = ["nmap", "-sS", "-O", target]
    result = subprocess.run(cmd, capture_output=True, text=True)

    with open(filename, "w") as f:
        f.write(result.stdout)

    print("✅ Scan complete.")
    print(f"📁 Result saved: {filename}\n")

    # ✅ Send alert
    send_to_telegram(f"🔍 Scan complete on {target}\n📁 Saved: {filename}")
