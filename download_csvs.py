import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

texas_zip_codes = [66666, 76065, 76065, 55555]

with webdriver.Chrome() as driver:
    # Loop over all the zip codes:
    for zip_code in texas_zip_codes:
        wait = WebDriverWait(driver, 10)
        driver.get("http://powertochoose.org/")
        driver.find_element(By.ID, "homezipcode").send_keys(zip_code)
        time.sleep(2)

        #On the site, if you input a bad zip code the style on this div is empty
        if driver.find_element(By.ID, "not-found").get_attribute("style") == '':
            #Click the close button if the bad zip message is displayed
            driver.find_element(By.CSS_SELECTOR, "a.btn-close").click()
            print('clicking off on zip', zip_code)
            continue

        #If you have a good zip then click to view results:
        else:
            print('About to click view results on ', zip_code)
            driver.find_element(By.ID, "view_all_results").click()
            # Keep checking for the presence of img to export results, then click it:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[title=\"Export results to Excel\"]"))).click()
            # Wait so that the browser can download the file:
            time.sleep(5)