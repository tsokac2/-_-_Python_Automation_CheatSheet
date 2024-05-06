<h1 align="center">Automating Emails</h1>

### Overview of the Section
* **[Sending a Single Email with Python](#sending-email)**
* **[Sending an Email Every Day at a Certain Time](#sending-email-dayli)**
* **[Sending Emails to a CSV List of Contacts](#sending-csv-emails)**
* **[Sending Emails with Attachments](#emails-attachments)**
* **[Send an Email with Modified Attachment](#emails-attachments-modify)**

### <a name=''></a>

#
### <a name="path-lib">Sending a Single Email with Python</a>

Here are the important points:

- library called ``yagmail`` to send emails from a Gmail account.
- You need to create a Gmail app password and store it as an environment variable before running the script.
- Here are the important commands:
    - ``import yagmail`` - imports the yagmail library
    - ``yag = yagmail.SMTP(user, password)`` - creates a SMTP object using your Gmail address and password
    - ``yag.send(to, subject, contents)`` - sends an email with the specified recipient, subject and content

**[Back To The Top](#Overview-of-the-Section)**
#
### <a name="sending-email-dayli">Sending an Email Every Day at a Certain Time</a>

Import ``datetime`` library as ``dt``: ``from datetime import datetime as dt``

```
* Use a loop to continuously check the time.
* Inside the loop:
    * Get the current time using `dt.now()`.
    * Extract the hour and minute using `.hour` and `.minute`.
    * Use an `if` statement to check if the current hour and minute match your desired time.
* If the condition is met (time matches), call the function to send the email.

**Important code:**

```python
if now.hour == 13 and now.minute == 15:  # Replace 13, 15 with your desired hour and minute
    # Your function to send email here
```
**Additional notes**:
- The script checks every minute by default. You can modify the loop interval for less frequent checks.
- Remember to replace the placeholder email content and recipient address with your own information.
- You'll need to configure your email credentials securely (not shown in the text).

**[Back To The Top](#Overview-of-the-Section)**
#
### <a name="sending-csv-emails">Sending Emails to a CSV List of Contacts</a>

**Important libraries**:
``pandas`` (used for working with CSV files)

**Code Snippets**:

1. **Reading CSV data into a Pandas DataFrame**:
    ```
    import pandas as pd

    df = pd.read_csv("contacts.csv")
    ```

2. **Iterating over rows in a DataFrame**:
    ```
    for index, row in df.iterrows():
    # your code here to process each row
    ```
3. **Accessing data from a specific column in a row**:
    ```
    email = row["email"]  # assuming "email" is the column name
    name = row["name"]  # assuming "name" is the column name
    ```

4. **Using f-strings for dynamic content**:
    ```
    contents = f"Hi {name}, {message}"
    ```
**Additional Notes**:
- The code uses secrets to store sensitive information like passwords.
- The script sends an email to each recipient listed in the "email" column of the CSV file.

**[Back To The Top](#Overview-of-the-Section)**
#
### <a name="emails-attachments">Sending Emails with Attachments</a>

**Libraries**:

``yagmail``: This library simplifies sending emails through Gmail in Python.

**Steps**:

1. **Set up Gmail app password**1. : You'll need to create an app password for your Gmail account and store it securely. This is because you shouldn't directly use your Gmail password in the code.
2. **Prepare your attachment**: Create a file (e.g., ``text.txt``) that you want to attach to the email.
3. **Import libraries and set variables**: In your Python code, import ``yagmail`` and set variables for the recipient's email address (e.g., using a disposable email service like dropmail.me) and the path to your attachment file.
4. **Construct the recipient list**: The ``yagmail`` library expects the recipient email in a list format. Even for a single recipient, you need to convert it to a list. Here's an example assuming the recipient email is stored in a variable named ``recipient_email``:

    ``recipient_list = [recipient_email]``

5. **Attach the file**: Add the path to your attachment file to the recipient list. The code will automatically handle attaching the file:
    ```
    recipient_list.append("text.txt")  # Assuming "text.txt" is your attachment filename
    ```
6. **Send the email**: Use ``yagmail`` to send the email with the recipient list and the content of your email (if any).

**Additional notes**:

- The video uses the ``contents`` variable, but the specific variable names might differ depending on your implementation.
- The video mentions handling attachment paths within folders. You'll need to provide the complete path (folder name and filename) if the attachment is not in the same directory as your Python script.

**[Back To The Top](#Overview-of-the-Section)**
#
### <a name="emails-attachments-modify">Send an Email with Modified Attachment</a>

**Concept**
- Script reads a CSV file containing email records (name, email, amount).
- Script sends an email to each record with a text file attached containing the amount owed.

**Important libraries**

- ``pandas`` (for handling CSV data)
- ``smtplib`` (for sending emails)

**Code Snippets**

1. **Generate Text File Function (``generate_file``)**:

- Takes file name and content as arguments.
- Opens the file in write mode (``'w'``).
- Writes the content to the file.
- Important: This function should likely be improved to avoid tight coupling with extensions (``".txt"``).

2. **Iterate through CSV dataframe**:

- Loops through each row of the dataframe.
- Calls ``generate_file`` to create a text file with the name (from the row) and amount (from the row).
- Constructs the email with recipient email, subject, body (including name and amount), and attachment filename (name+".txt").
- Sends the email using ``smtplib``.

**Additional Notes**

- The video mentions converting the amount (integer) to a string before writing it to the text file ``(str_content = str(amount))``
- You'll need to replace placeholders like sender email, password, and CSV file path with your own information.
- The script uses an app password for Gmail login, not the regular password.

**[Back To The Top](#Overview-of-the-Section)**
#