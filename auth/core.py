from utils.banner import show_banner
from modules.scanner import scan_target
from auth.license import validate_key

def main():
    show_banner()
    
    if not validate_key():
        return  # exit if key is wrong

    target = input("🧠 Enter IP or domain to scan: ").strip()
    
    if target:
        scan_target(target)
    else:
        print("⚠️ No target entered.")

if __name__ == "__main__":
    main()
