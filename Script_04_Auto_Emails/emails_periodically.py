import yagmail
import os
import time

SENDER = 'tsokac2@gmail.com'
RECEIVER = 'bladezero3@gmail.com'

subject = 'This is the subject'
contents = """
Here is the content of the email
Hi!
"""
while True:
    yag = yagmail.SMTP(user.SENDER, password=os.getenv('PASSWORD'))
    yag.send(to=RECEIVER, subject=subject, contents=contents)
    print("Email Sent!")
    time.sleep(60)