from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    # Set option to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://titan22.com/")
    return driver


def main():
    driver = get_driver()
    driver.find_element(by="id", value="CustomerEmail").send_keys("user@email.com")
    time.sleep(2)
    driver.find_element(by="id", value="CustomerPassword").send_keys("<your_password>" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath", value="<copy_full_path_value_from_the_chrome_dev_tools").click()
    print(driver.current_url)   

print(main())