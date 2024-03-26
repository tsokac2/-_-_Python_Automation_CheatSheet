

# Web Source:  The World Clock — Worldwide - https://www.timeanddate.com/worldclock/
from selenium import webdriver
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
    driver.get("https://www.timeanddate.com/worldclock/")
    return driver


# def clean_text(text):
#     """Extract only the seconds from the world clock website"""
#     output = float(text.split(": ")[])
#     return output


def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[6]/section[1]/div/div[1]/div[1]/div/div[4]/span/span/span[4]")
    # return clean_text(element.text)
    return element

print(main())