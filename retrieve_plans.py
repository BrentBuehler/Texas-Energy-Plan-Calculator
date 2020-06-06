import time
import datetime
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


def enter_zip(code):
    driver.find_element(By.ID, "homezipcode").send_keys(code)


def get_results_and_download():
    # If you have a good zip then click to view results:
    driver.find_element(By.ID, "view_all_results").click()
    # Keep checking for the presence of img to export results, then click it:
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[title=\"Export results to Excel\"]"))).click()


def check_for_dropdown():
    if driver.find_element_by_css_selector('#distributors').find_elements_by_tag_name("option"):
        return True


# If zip code has multiple distributors, download plans for each dropdown option
def download_dropdown_options(zip_code_with_dropdown):
    element = driver.find_element_by_css_selector('#distributors')
    all_options = element.find_elements_by_tag_name("option")
    list_of_options = []
    get_option_loop_count = 0
    # Loop over all options in dropdown and append to a list we can loop over and download plans for each
    for option in all_options:
        # Skip first placeholder option:
        if get_option_loop_count == 0:
            get_option_loop_count += 1
            continue
        list_of_options.append(option.get_attribute("text"))

    download_option_loop_count = 0
    for dropdown_option in list_of_options:
        # On first loop pass, we only need to click the first option and download
        if download_option_loop_count == 0:
            driver.find_element_by_xpath("//select[@id='distributors']/option[text()='" + dropdown_option + "']").click()
            get_results_and_download()
            download_option_loop_count += 1
            print("Downloaded distributor", dropdown_option, "for zip code", zip_code_with_dropdown)
            continue
        # Otherwise get new page and continue with next options:
        driver.get("http://powertochoose.org/")
        enter_zip(zip_code)
        time.sleep(1)
        driver.find_element_by_xpath("//select[@id='distributors']/option[text()='" + dropdown_option + "']").click()
        time.sleep(1)
        get_results_and_download()
        print("Downloaded distributor", dropdown_option, "for zip code", zip_code_with_dropdown)


def check_for_invalid_zip():
    # This div's style attribute is empty when a bad zip is present, so test for this
    if driver.find_element(By.ID, "not-found").get_attribute("style") == '':
        return True


start_time = datetime.datetime.now()

with webdriver.Chrome() as driver:
    # Loop over all the zip codes, inputting them in search box:
    for zip_code in texas_zip_codes:
        wait = WebDriverWait(driver, 10)
        driver.get("http://powertochoose.org/")
        try:
            enter_zip(zip_code)
        except:
            print('Error at zip code', zip_code)
            continue
        time.sleep(1)

        if check_for_dropdown():
            print("Multiple distributors found at zip", zip_code)
            download_dropdown_options(zip_code)
            continue

        if check_for_invalid_zip():
            # If site can't find zip, close modal and retry with next zip
            driver.find_element(By.CSS_SELECTOR, "a.btn-close").click()
            print('Couldnt find zip code', zip_code)
            continue

        get_results_and_download()

    # Wait a bit for last file to download before closing window:
    time.sleep(5)

    runtime = datetime.datetime.now() - start_time
    runtime_minutes = int(round(runtime.total_seconds() / 60))
    print('The script took', runtime_minutes, 'minutes!')