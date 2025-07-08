from license import verify_license
from modules.banner import show_banner
from modules.scanner import scan_target

def main():
    show_banner()
    key = input("🔐 Enter License Key: ").strip()
    if not verify_license(key):
        print("❌ Invalid license key. Access denied.")
        return

    target = input("🧠 Enter IP or domain to scan: ")
    scan_target(target)

if __name__ == "__main__":
    main()
