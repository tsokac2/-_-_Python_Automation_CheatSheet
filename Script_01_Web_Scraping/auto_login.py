# Webpage source: https://onlinesim.io/auth/login?redirect=/v2/numbers

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
    driver.get("https://onlinesim.io/auth/login?redirect=/v2/numbers")
    return driver


def main():
    driver = get_driver()
    driver.find_element(by="id", value="login").send_keys("<email")
    # Entering the <password> value and click to the "Login" button
    driver.find_element(by="id", value="password").send_keys("<password>" + Keys.RETURN)
    # After succesfull login - navigate to any page in the platform dashboard
    # driver.find_element(by="xpath", value="/html/body/div[2]/div[2]/div[2]/div/div/form/div[4]/button").click()
    print(driver.current_url)

  
print(main())


