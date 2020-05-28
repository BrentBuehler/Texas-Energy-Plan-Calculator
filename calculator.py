import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

texas_zip_codes = [75019, 75039, 75038]

with webdriver.Chrome() as driver:
    # Loop over all the zip codes:
    for zip_code in texas_zip_codes:
        wait = WebDriverWait(driver, 10)
        # Get the url:
        driver.get("http://powertochoose.org/")
        # Find zip code box and input zip code:
        driver.find_element(By.ID, "homezipcode").send_keys(zip_code)
        # Click the View All Results button:
        driver.find_element(By.ID, "view_all_results").click()
        # Keep checking for the presence of img to export results, then click it:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[title=\"Export results to Excel\"]"))).click()
        # Wait so that the browser can download the file:
        time.sleep(5)