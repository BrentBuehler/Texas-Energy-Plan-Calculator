import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Load file and grab first column:
zip_code_database = np.loadtxt(fname='zip_code_database 6.1.csv', delimiter=',', usecols=(0,), skiprows=1)
zip_codes = zip_code_database[0:]

# Loop over each value and create list, convert to python dtype
texas_zip_codes = []
for code in zip_codes:
    texas_zip_codes.append(np.int(code))

with webdriver.Chrome() as driver:
    # Loop over all the zip codes, inputting them in search box:
    for zip_code in texas_zip_codes:
        wait = WebDriverWait(driver, 10)
        driver.get("http://powertochoose.org/")
        try:
            driver.find_element(By.ID, "homezipcode").send_keys(zip_code)
        except:
            print('Error at zip code', zip_code)
            continue
        time.sleep(1)

        # A div's style attribute is empty when a bad zip is present, so test for this
        if driver.find_element(By.ID, "not-found").get_attribute("style") == '':
            # Click the close button if the bad zip message is displayed and continue loop
            driver.find_element(By.CSS_SELECTOR, "a.btn-close").click()
            print('Couldnt find zip code', zip_code)
            continue

        # If you have a good zip then click to view results:
        else:
            driver.find_element(By.ID, "view_all_results").click()
            # Keep checking for the presence of img to export results, then click it:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[title=\"Export results to Excel\"]"))).click()

    # Wait a bit for last file to download before closing window:
    time.sleep(5)