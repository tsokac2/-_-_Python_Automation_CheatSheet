import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase 

SENDER = 'youremail@hotmail.com'
RECEIVER = 'receiver@gmail.com'
PASSWORD = '<import_from_env_enviroment>' # os.getenv('PASSWORD')

message = MIMEMultipart()
message['From'] = SENDER
message['To'] = RECEIVER
message['Subject'] = 'Hello again!'

body = """
<h2>Hi There </h2>
Today is a very nice day!
Let's hope for more!
"""

mimetext = MIMEText(body, 'html')
message.attach(mimetext)


# Adding attachment logic

attachment_path = "<defin_file_path>"
attachment_file = open(attachment_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(attachment_file.read())
payload.add_header('Conten-Disposition', 'attachment', filename=attachment_path)
message.attach(payload)


SERVER = smtplib.SMTP('smtp.office365.com', 587)
SERVER.startls()
SERVER.login(SENDER, PASSWORD)
message_text = message.as_string()
print(message_text)
SERVER.sendmail(SENDER, RECEIVER, message_text)
SERVER.quit()
