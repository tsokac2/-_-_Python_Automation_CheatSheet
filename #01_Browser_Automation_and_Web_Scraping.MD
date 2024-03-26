<h1 align="center">Browser Automation and Web Scraping</h1>

### Overview of the Section
* **[Scraping with Selenium](#selenium)**
* **[Automate Login Process](#auto-login)**

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