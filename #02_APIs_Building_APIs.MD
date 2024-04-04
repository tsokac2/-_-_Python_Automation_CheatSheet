<h1 align="center">Accessing APIs | Building APIs</h1>

### Overview of the Section
* **[REST APIs and Python](#rest-python)**
* **[Building a Custom API with Flask](#custom-api)**
* **[Facebook Graph API](#fb-api)**

#
### <a name="rest-python">REST APIs and Python</a>

- REST APIs are a way for applications to communicate with each other.
- They provide data in a structured format (like JSON) that is easy for computers to understand.
- To access data from an API in Python, you can use the requests library.
- The code uses the ``.get()`` method from the requests library to make a GET request to the API URL.
- The URL may contain parameters that specify what data you want to retrieve.
- Some APIs require an API key to access their data.

**Important code**:

- ``requests.get(url)``: This code makes a GET request to the specified URL.
- ``.json()``: This method converts the response from the API to a Python dictionary.
- Accessing data within the dictionary using its keys and indexes.

**[Python Request Docs](https://docs.python-requests.org/en/latest/)**

**[Back To The Top](#Overview-of-the-Section)**
#
### <a name="custom-api">Building a Custom API with Flask</a>
- This video tutorial guides you through creating an API that provides currency exchange rates.
- **Framework**: Flask (lightweight web framework for Python)
- **Library for scraping data**: Beautiful Soup
- **Sample API endpoint**: ``/api/v1/<input_currency>-<output_currency> (e.g., /api/v1/USD-JPY)``

**Key Code Snippets**:
```
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    # Return documentation for the API
    pass

@app.route("/api/v1/<input_currency>-<output_currency>")
def get_currency_rate(input_currency, output_currency):
    # Code to scrape exchange rate data using Beautiful Soup
    # ...
    rate = get_currency(input_currency, output_currency)
    result = {
        "input_currency": input_currency,
        "output_currency": output_currency,
        "rate": rate
    }
    return jsonify(result)

# ... (app running code)
```
**Sample function to scrape currency data (implementation details omitted):**
```
def get_currency(input_currency, output_currency):
    # Code to fetch and parse data from a website like 'Exchangerates'
    # ...
    rate = ...  # Extracted exchange rate
    return rate
```
**[Back To The Top](#Overview-of-the-Section)**
#

### <a name="fb-api">Facebook Graph API</a>

1. **Using the Official Facebook API via Python**:
    - Introduces accessing Facebook profiles via Python using the official Facebook API.
    - Emphasizes that the process is compliant with Facebook's rules and not about hacking.
    - Highlights the benefit of batch accessing data like photos, videos, posts, and comments.

2. **Creating a Facebook Developer Account**:
    - Instructs to navigate to developers.facebook.com and create a developer account to access Facebook data programmatically.
    - Guides through the process of registration, including verifying phone number and email address.
    - Explains the necessity of creating a Facebook app to access data.

3. **Generating Access Token**:
    - Demonstrates generating an access token through the Graph API Explorer.
    - Notes the security feature where newly created Facebook accounts may need to wait for 60 minutes before generating the access token.

4. **Interacting with Graph API Explorer**:
    - Shows how to use the Graph API Explorer interface to interact with Facebook's API.
    - Demonstrates querying data such as user ID and name, user posts, and photos.
    - Illustrates how to generate access tokens for specific permissions.

5. **Accessing Data via Python**:
    - Provides code snippets to access Facebook data via Python using the requests library.
    - Explains constructing URLs for API requests and handling response data.
    - Shows how to access user posts and photos, including iterating over dictionaries to extract specific information.

6. **Downloading Images**:
    - Guides on downloading images from Facebook via Python, including extracting image URLs and saving images locally.

7. **Exploring API Documentation**:
    - Mentions accessing Facebook Graph API reference documentation for more detailed information on available endpoints and fields.

8. **Conclusion**:
    - Concludes by encouraging further exploration of the Facebook API and its limitless possibilities.
    - Encourages revisiting the video as a starting point for working with the Facebook API.

**[Back To The Top](#Overview-of-the-Section)**