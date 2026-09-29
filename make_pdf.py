import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1280, "height": 720})
        
        html_path = os.path.abspath(r"C:\Users\shieru_k\2026-Hoken\suishitsu-odaku-chita.html")
        url = f"file:///{html_path}?print-pdf"
        
        print(f"Loading {url}...")
        await page.goto(url, wait_until="networkidle")
        await page.wait_for_timeout(2000)
        
        pdf_path = r"C:\Users\shieru_k\2026-Hoken\slides.pdf"
        await page.pdf(
            path=pdf_path,
            print_background=True,
            landscape=True,
            width="1280px",
            height="720px",
            margin={"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"}
        )
        print(f"PDF saved to {pdf_path}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
