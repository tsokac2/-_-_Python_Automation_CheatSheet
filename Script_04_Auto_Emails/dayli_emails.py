import yagmail
import os
import time
from datetime import datetime as dt

SENDER = 'email_sender@mail.com'
RECEIVER = 'email_receiver@mail.com'

subject = 'This is the subject'
contents = """
Here is the content of the email
Hi!
"""
while True:
    now = dt.now()
    if now.hour == 13 and now.minute == 15:
        yag = yagmail.SMTP(user.SENDER, password=os.getenv('PASSWORD'))  # PASSWORD value stored in env file
        yag.send(to=RECEIVER, subject=subject, contents=contents)
        print("Email Sent!")
        time.sleep(60)