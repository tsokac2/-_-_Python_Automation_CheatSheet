import yagmail
import os

SENDER = 'email_sender@mail.com'
RECEIVER = 'email_receiver@mail.com'

subject = 'This is the subject'
contents = """
Here is the content of the email
Hi!
"""

yag = yagmail.SMTP(user=SENDER, password=os.getenv('PASSWORD')) # PASSWORD value stored in env file
yag.send(to=RECEIVER, subject=subject, contents=contents)
print("Email Sent!")