from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ✅ Set your chromedriver.exe path here:
service = Service("C:\\Users\\admin\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.amazon.in")  # Use .in for India version

try:
    # ✅ Wait until the search box appears
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))

    search_box.send_keys("headphones")
    search_box.submit()

    # ✅ Wait for results to load
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".s-main-slot")))
    print("✅ Search completed.")

    # ✅ Print number of results
    results = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")
    print(f"🔍 Number of products found: {len(results)}")

except Exception as e:
    print("❌ ERROR:", e)

finally:
    time.sleep(5)
    driver.quit()
