import yagmail
import os
import pandas

SENDER = 'email_sender@mail.com'
subject = 'This is the subject'

yag = yagmail.SMTP(user.SENDER, password=os.getenv('PASSWORD')) # PASSWORD value stored in env file
df = pandas.read_csv('contacts.csv')
print(df)

for index, row in df.iterrows():
    contents = f""" Hi {row['name']} 
    Here is the content of the email
    Hi!
    """
    yag.send(to=row['email'], subject=subject, contents=contents)
    print("Email Sent!")