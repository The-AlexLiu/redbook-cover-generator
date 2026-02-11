import argparse
from playwright.sync_api import sync_playwright
import os

def generate_image(title, date, output_path="Demo_01.jpg", auto_open=True):
    # Current directory
    current_dir = os.getcwd()
    file_url = f"file://{current_dir}/index.html"
    
    # URL with parameters
    url = f"{file_url}?title={title}&date={date}"
    
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch()
        # Set viewport to exact dimensions required
        # Note: device_scale_factor=2 ensures high resolution (Retina-like quality) 
        # but output might be double size if we don't handle it. The user wants 1242x1656.
        # So we set viewport 1242x1656 and scale=1.
        page = browser.new_page(viewport={"width": 1242, "height": 1656})
        
        print(f"Opening: {url}")
        page.goto(url)
        
        # Taking screenshot of the #capture element or full page
        # Since body is 1242x1656, full_page=True works perfectly.
        page.screenshot(path=output_path, full_page=True, type="jpeg", quality=90)
        
        print(f"Generated: {output_path} (1242x1656)")
        browser.close()
    
    # Automatically open the image on macOS for instant preview
    if auto_open:
        try:
            import subprocess
            subprocess.run(["open", output_path])
            print(f"Opened {output_path} in preview.")
        except Exception as e:
            print(f"Could not auto-open image: {e}")
            
    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Redbook Title Page Image")
    parser.add_argument("--title", default="收视冠军", help="Main title text")
    parser.add_argument("--date", default="2月9日～2月15日", help="Date range text")
    parser.add_argument("--output", default="Demo_01.jpg", help="Output filename")
    
    args = parser.parse_args()
    
    generate_image(args.title, args.date, args.output, auto_open=True)
