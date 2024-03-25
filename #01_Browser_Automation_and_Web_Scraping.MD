<h1 align="center">Browser Automation and Web Scraping</h1>

### Overview of the Section
* **[Scraping with Selenium](#selenium)**



#
### <a name="selenium">Scraping with Selenium</a>

**Libraries:**

Selenium - a Python library used to automate browser actions **[pip install selenium](https://pypi.org/project/selenium/)**
webdriver - a tool from Selenium to interact with web browsers

**[WebDriver Documentation](https://www.selenium.dev/documentation/webdriver/)**

**How to find the XPath**:

1. Right-click on the element you want to scrape and select "Inspect element".
2. In the developer tools, right-click on the element tag and select "Copy" -> "Copy XPath".
3. Paste the copied XPath into the ``value`` argument of ``find_element``.

**Note**:

- The code uses ``find_element`` which is deprecated. It's recommended to use ``find_element.by.XPATH`` instead.
- Remember to replace ``"https://www.example.com"`` with the actual URL of the website you want to scrape.
- You will need to find the correct XPath for the specific element containing the text you want to scrape.

**[Back To The Top](#Overview-of-the-Section)**
#