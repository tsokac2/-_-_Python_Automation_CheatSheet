import yagmail
import os
import time

SENDER = 'email_sender@mail.com'
RECEIVER = 'email_receiver@mail.com'

subject = 'This is the subject'
contents = """
Here is the content of the email
Hi!
"""
while True:
    yag = yagmail.SMTP(user.SENDER, password=os.getenv('PASSWORD'))  # PASSWORD value stored in env file
    yag.send(to=RECEIVER, subject=subject, contents=contents)
    print("Email Sent!")
    time.sleep(60)