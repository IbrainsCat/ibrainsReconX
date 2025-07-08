import subprocess
from datetime import datetime
import os
import requests
from fpdf import FPDF  # PDF generator

# 📤 Send file to Telegram
def send_to_telegram(filename):
    bot_token = "7391587044:AAEotUi0bMimDIiK2Qa82dMuzkuI4JQzNsc"
    chat_id = "7600608772"
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    with open(filename, "rb") as f:
        try:
            requests.post(url, data={"chat_id": chat_id}, files={"document": f})
        except:
            print("⚠️ Telegram upload failed.")

# 📄 Generate PDF from scan result
def generate_pdf(text, output_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Courier", size=10)
    for line in text.splitlines():
        pdf.cell(0, 5, txt=line, ln=1)
    pdf.output(output_filename)

# 🔍 Main scan logic
def scan_target(target):
    print("🔧 Select scan type:")
    print("[1] Full Scan")
    print("[2] Top 100 Ports")
    print("[3] Network Sweep")
    choice = input(">> ").strip()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"scan_results/{target}_{timestamp}.txt"

    if choice == "3":
        print(f"📡 Sweeping subnet: {target}...\n")
        cmd = ["nmap", "-sn", target]
    elif choice == "2":
        print(f"🛰️ Scanning top 100 ports on {target}...\n")
        cmd = ["nmap", "-Pn", "-sV", "--top-ports", "100", "--open", target]
    else:
        print(f"🛰️ Scanning full ports on {target}...\n")
        cmd = ["nmap", "-Pn", "-sV", "--open", target]

    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        result = e.output
        print("⚠️ Nmap scan failed.")

    with open(filename, "w") as f:
        f.write(result)

    print("✅ Scan complete.")
    print(f"📁 Result saved: {filename}\n")

    # 🔐 Telegram Upload (Text)
    send_to_telegram(filename)

    # 📄 Generate and Send PDF
    try:
        pdf_file = filename.replace(".txt", ".pdf")
        generate_pdf(result, pdf_file)
        print(f"📄 PDF report saved: {pdf_file}")
        send_to_telegram(pdf_file)
    except:
        print("⚠️ PDF generation failed.")
