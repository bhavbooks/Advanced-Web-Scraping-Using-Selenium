from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import random
import time

options = webdriver.ChromeOptions()

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")

time.sleep(random.uniform(2, 2.5))

# 2. FIX: Using more stable selectors (Google's main input is usually name="q")
try:
    user_input = driver.find_element(By.NAME, "q")
    user_input.send_keys("campusX")
    time.sleep(1)
    user_input.send_keys(Keys.ENTER)
    
    time.sleep(2) # Wait for results to load

    # 3. FIX: Clicking the link. Instead of find_element for <cite>, 
    # find the <h3> or the <a> tag which is the actual clickable link.
    first_link = driver.find_element(By.CSS_SELECTOR, "h3") 
    first_link.click() 
    
    time.sleep(3) # Wait for CampusX page to load

    # 4. FIX: Price extraction. XPaths with IDs like "169839..." change every session.
    # You should use a relative XPath or a Class Name.
    # Assuming you want to screenshot a specific element:
    price_element = driver.find_element(By.XPATH, "//span[contains(text(), '₹') or contains(text(), '$')]")
    
    # Correct way to take a screenshot of an element
    price_element.screenshot('price_screenshot.png')
    print("Screenshot saved successfully!")

except Exception as e:
    print(f"An error occurred: {e}")