import yagmail
import os
import pandas

SENDER = 'email_sender@mail.com'

yag = yagmail.SMTP(user=SENDER, password=os.getenv('PASSWORD')) # PASSWORD value stored in env file
df = pandas.read_csv('contacts_attachments.csv')

def generate_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

for index, row in df.iterrows():
    name = row['name']
    filename = name + ".txt"
    amount = row['amount']
    receiver_email = row['email']

    generate_file(filename, amount)

    subject = "This is the subject!"
    contents = [f""" 
    Hey, {name} you have to pay {amount}
    Bill is attached!""",
    filename,
    ]

    yag.send(to=receiver_email, subject=subject, contents=contents)
    print["Email Sent"]