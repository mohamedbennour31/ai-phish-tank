import asyncio
import os
from playwright.async_api import async_playwright

async def capture_site(url):
    # PREVENT STALE DATA: Delete the old screenshot if it exists
    if os.path.exists("screenshot.png"):
        os.remove("screenshot.png")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"
        )
        page = await context.new_page()
        
        print(f"[*] Visiting: {url}")
        try:
            # CHANGE: Use 'load' instead of 'networkidle' to avoid timeouts on heavy sites
            await page.goto(url, wait_until="load", timeout=30000)
            # Give it 2 seconds just to settle
            await asyncio.sleep(2) 
            await page.screenshot(path="screenshot.png")
            print("[+] Screenshot saved as screenshot.png")
        except Exception as e:
            print(f"[!] Capture Error: {e}")
        
        await browser.close()
