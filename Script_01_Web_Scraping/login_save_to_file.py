# Webpage source: https://onlinesim.io/auth/login?redirect=/v2/numbers

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt


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


def clean_text(text):
    # Extract only the temperature from text
    output = float(text.split(": "[1]))
    return output

def write_file(text):
    # Write input text into a text file
    filename = f"dt.now.strftime('%Y-%m-%d.%H-%M-%S")}.txt')
    with open(filename, 'w') as file:
        file.write(text)


def main():
    driver = get_driver()
    time.sleep(2)
    while True:
       time.sleep(2)
       element = driver.find_element(by="xpath", value="")
       text =  clean_text(element.text)
       write_file(text)


print(main())