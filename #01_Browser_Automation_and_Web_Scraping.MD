<h1 align="center">Browser Automation and Web Scraping</h1>

### Overview of the Section
* **[Scraping with Selenium](#selenium)**
* **[Automate Login Process](#auto-login)**
* **[Beautiful Soup for Web Scraping](#bs4)**

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

### <a name="auto-login">Automate Login Process</a>

**Objective**: Write a script to log in to a form with a username and password, then click on the home page.

**URL for Logging In**: The URL for logging in is ``automated.pythonanywhere.com/login/``.

**Credentials**: The username and password are both "automatedautomated".

**Script Setup**:
- Use Selenium WebDriver.
- Define a function to get the driver, initially pointing to the homepage.
- Modify the driver's URL to the login page.

**Locating Elements**:
-Locate the username input box using its ID: id_username.
- Locate the password input box using its ID: id_password.

**Entering Data**:
- Use send_keys() to input the username and password into their respective input boxes.
- Import time to introduce a delay between actions, enhancing reliability.

**Submitting the Form**:
- Press the "Enter" key after inputting the password to submit the form.
- Import ``keys`` from ``selenium.webdriver.common.keys`` to access the "Enter" key.

**Verifying Login**:
- Check the current URL after logging in to ensure successful navigation.

**Navigating to Home Page**:
- Locate and click the home button using XPath, as it doesn't have an ID.
- Introduce a delay before clicking to ensure smooth execution.

**Further Steps**:
In future iterations, plan to extract data from the logged-in page.

Overall, the script automates the login process by filling in the credentials, submitting the form, and navigating to the desired page, demonstrating the basics of web scraping and automation using Selenium WebDriver.

**[Back To The Top](#Overview-of-the-Section)**
#

### <a name="bs4">Beautiful Soup for Web Scraping</a>

**Extracting Currency Rates with Beautiful Soup**

- We'll use https://www.x-rates.com/ to s real-time currency exchangrates.
- The script will take two currencies as input and construct a URL for the specific conversion.
- Beautiful Soup will then parse the HTML content of the webpage.

**Key Steps and Code**

1. Install libraries:
- ``requests`` - to fetch the webpage content.
- ``beautifulsoup4`` - to parse the HTML content.
2. Define a function ``get_currency`` that takes two arguments:
- ``from_currency``: The starting currency code (e.g., EUR).
- ``to_currency``: The target currency code (e.g., USD).
3. Construct the URL for the specific currency conversion.
4. Use ``requests.get`` to get the webpage content.
5. Parse the content using ``BeautifulSoup`` with HTML parser.
6. Find the element containing the exchange rate (likely a span element with a specific class).
7. Extract the text content of the element using ``.get_text()`` method.
8. Clean the extracted text to remove unnecessary characters (e.g., currency symbol).
9. Convert the cleaned text to a float data type.
10. The function should return the final exchange rate as a float.

**[Back To The Top](#Overview-of-the-Section)**
