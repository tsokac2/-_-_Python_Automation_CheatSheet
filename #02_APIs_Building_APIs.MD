<h1 align="center">Accessing APIs | Building APIs</h1>

### Overview of the Section
* **[REST APIs and Python](#rest-python)**

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


**[Back To The Top](#Overview-of-the-Section)**
#