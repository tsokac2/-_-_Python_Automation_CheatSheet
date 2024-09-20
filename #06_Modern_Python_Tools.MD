<h1 align="center">Modern Python Tools</h1>

### Overview of the Section
* **[Create and Publish a Website with Python in 2 Minutes](#flask)**
* **[Streamlit](#streamlit)**
* **[PythonAnywhere](#pyany)**

#
#### Popularity of Python
Python's widespread popularity in the last five years has led to the development of many modern tools designed to assist Python programming.

#### Modern Tools
These tools facilitate tasks like:
Publishing Python websites easily.
Creating and publishing articles with embedded Python code.
Developing and sharing data visualizations online.

#### Cloud-Based Tools
Many of these modern tools are cloud-based, offering an alternative to traditional local programming.

#### Traditional Programming
Despite the rise of cloud-based tools, traditional local programming remains valuable for privacy and security.

#### Importance of Modern Tools
Knowledge of these cutting-edge tools is essential for making programming more productive and enjoyable.

#### Learning Objective
The section focuses on introducing and teaching how to use these modern tools alongside Python.

#
**[Back To The Top](#Overview-of-the-Section)**

### <a name="flask">Create and Publish a Website with Python in 2 min</a>

#### Setting Up Flask:

Flask is a simple Python web framework, preferred over Django for quick website creation.

Import Flask in your main.py file:
``from flask import Flask``

#### Creating a Flask Application:

Instantiate a Flask object:
``app = Flask(__name__)``

Define URL routes using decorators:
```@app.route("/")
def home():
    return "Welcome to my website"
For each webpage, create a new route and function.
```

#### Running the Flask Application:
Use the run method to start the app:
```
if __name__ == "__main__":
    app.run(host='0.0.0.0')
```

#### Website Access and Maintenance:
The website remains live even after you close Repl.it.
For local deployment, manual publishing is required using services like Digital Ocean or PythonAnywhere.

#### Website Content:
The example uses a simple string for content, but in practice, you should use HTML to add images, headings, and styles.

#### Further Learning:
The course includes a more detailed lecture on creating web apps with Flask, searchable by the keyword "Flask."

This summary covers the essentials of creating and deploying a basic website using Flask on Repl.it, highlighting key commands, practices, and further learning resources.

#
**[Back To The Top](#Overview-of-the-Section)**

### <a name="streamlit">Create and Publish Web Apps and Data Dashboards with Streamlit</a>

The text introduces Streamlit, a Python framework that allows users to create interactive web apps and data visualization dashboards quickly and easily.

#### Introduction to Streamlit:

* Streamlit is a new, free framework that lets you build Python web apps and dashboards and deploy them instantly.
* The apps are public immediately as the framework is tied to a cloud service.

#### Setting Up a Simple Web App:

* Import Streamlit: Use import streamlit as st (commonly referred to as st).
* Add a Title and Subheader:

```
st.title("Our first Streamlit app")
st.subheader("Introducing Streamlit to automate everything with Python")
st.text("This is our first web app.")
```

#### Running the App:
Normally, to run the app locally, you use the command:

``streamlit run main.py``

#### Deploying the App:

* You need a GitHub account.
* Upload your code to GitHub.
* Use Streamlit Share to deploy the app by authorizing Streamlit to connect with your GitHub account.
* Deploy the app using the repository’s URL. The app will then be accessible via a public URL.

#### Adding a DataFrame and Graphs:

```
import pandas as pd
data = {"Series1": [1, 3, 4, 5, 7], "Series2": [10, 30, 40, 100, 250]}
df = pd.DataFrame(data)
st.write(df)
st.line_chart(df) # Add a Line Chart
```

#### Adding Interactivity with Widgets:
```
my_slider = st.slider("Celsius", 0, 100)
st.write(f"In Fahrenheit: {my_slider * 9/5 + 32}")
```
Commit and push the changes to GitHub to update the public URL.

#
**[Back To The Top](#Overview-of-the-Section)**

### <a name="pyany">PythonAnywhere</a>

#### 1. Introduction to PythonAnywhere:
* PythonAnywhere is a service that gives you access to servers running 24/7.
* You can write and run Python code, install Python libraries and Linux apps, and deploy web apps.
* Schedule tasks: Automate Python script execution at specific times.

#### 2. Key Features:
* Write and Run Python Code:

    * After creating an account, access the dashboard to start coding.
    * To create a Python console, go to Consoles and select a Python version (e.g., Python 3.8). This opens an interactive Python shell.

* Install Python Libraries:

Open a Bash console to install libraries:

``pip3.8 install speechrecognition``

* After installation, import the library in the Python console:

    ``import speech_recognition``

* Create Python Files:
    * Go to Files > New File to create a Python script (e.g., hello.py).
    * Write Python code in the file and execute it using the Run button.

* Deploy Web Apps:
    * Under the Web menu, upload and deploy your web apps.
    * Note: For free accounts, web apps expire every three months, requiring a manual refresh.

* Schedule Tasks:
    * In the Tasks menu, you can schedule Python scripts to run at specific times daily.
    * Example:

        * Upload your Python script (e.g., hello.py) to the Files section.
        * Note the file path: /home/your_username/hello.py.
        * In Tasks, specify the script’s path and the execution time (in UTC).
            ```
            Path to script: /home/your_username/hello.py
            Execution time: 10:00 UTC
            ```

#### 3. Additional Features:
* MySQL Databases: Available for free; PostgreSQL requires a paid plan.
* PythonAnywhere is useful for automating tasks like sending emails or scraping data at scheduled intervals.

#### 4. Limitations:
Free accounts have limitations, such as the number of consoles you can open and the need to refresh web apps every three months.

#### 5. Conclusion:
PythonAnywhere is a valuable tool for running Python code continuously, automating tasks, and deploying web apps without the need for your own server.

**[Back To The Top](#Overview-of-the-Section)**