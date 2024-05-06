<h1 align="center">Automating Emails</h1>

### Overview of the Section
* **[Sending a Single Email with Python](#sending-email)**

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


**[Back To The Top](#Overview-of-the-Section)**
#