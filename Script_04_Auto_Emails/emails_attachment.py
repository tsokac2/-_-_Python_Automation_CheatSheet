import yagmail
import os

SENDER = 'email_sender@mail.com'
RECEIVER = 'email_receiver@mail.com'

subject = 'This is the subject'

contents = ["""
Here is the content of the email
Hi!
""", 'text_attachment.txt'] # Make sure to define correct file path - sample_folder/file.txt

yag = yagmail.SMTP(user=SENDER, password=os.getenv('PASSWORD')) # PASSWORD value stored in env file
yag.send(to=RECEIVER, subject=subject, contents=contents)
print("Email Sent!")