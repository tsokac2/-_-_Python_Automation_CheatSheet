import smtplib

SENDER = 'youremail@hotmail.com'
RECEIVER = 'receiver@gmail.com'
PASSWORD = '<import_from_env_enviroment>' # os.getenv('PASSWORD')

message = """\
Subject: Hello Hello

This is Tom!
Just wanted to say hi!
"""

SERVER = smtplib.SMTP('smtp.office365.com', 587)
SERVER.startls()
SERVER.login(SENDER, PASSWORD)
SERVER.sendmail(SENDER, RECEIVER, message)
SERVER.quit()
