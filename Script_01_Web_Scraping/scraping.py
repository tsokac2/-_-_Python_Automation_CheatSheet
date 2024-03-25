from selenium import webdriver
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
    driver.get("https://www.tomislavsokac.com/home")
    return driver


def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[2]/div/div/div[3]/div/div[2]/div[1]/h1")
    return element.text

print(main())