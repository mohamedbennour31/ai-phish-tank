import asyncio
import os
from capture import capture_site
from analyze import analyze_phish
from enrich import check_domain_age

async def full_audit(url):
    print(f"\n{'='*60}")
    print(f"🛡️  AI PHISH-TANK: FULL SECURITY AUDIT")
    print(f"Target: {url}")
    print(f"{'='*60}")
    
    # 1. Evidence Collection
    await capture_site(url)
    
    # 2. Technical OSINT
    print("\n[*] Researching technical metadata...")
    check_domain_age(url)
    
    # 3. Visual Intelligence - NOW PASSING THE REAL URL
    if os.path.exists("screenshot.png"):
        print("\n[*] Initializing AI Vision Analysis...")
        analyze_phish('screenshot.png', url) # Pass the URL here!
    else:
        print("\n[!] AI Analysis skipped: No screenshot captured.")
    
    print(f"\n{'='*60}")
    print("✅ AUDIT COMPLETE")
    print(f"{'='*60}")

if __name__ == "__main__":
    print("\n" + " " * 15 + "🛡️  WELCOME TO AI PHISH-TANK 🛡️")
    
    try:
        user_url = input("🔗 Enter the URL to investigate: ").strip()
        if user_url:
            if not user_url.startswith("http"):
                user_url = "https://" + user_url
            asyncio.run(full_audit(user_url))
        else:
            print("[!] No URL provided.")
    except KeyboardInterrupt:
        print("\n[!] Stopped.")
