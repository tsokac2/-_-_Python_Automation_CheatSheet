import os
from twilio.rest import Client
import time
from datetime import datetime as dt

account_sid = os.environ['TWILLIO_ACCOUNT_SID']
auth_token  = os.environ['TWILLIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

while True:
    now = dt.now()
    if now.hour == 13 and now.minute == 18:
        message = client.messages \
                        .create(
                            body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                            from_='+1000000000'
                            to='+2000000000'
                        )
        print(message.sid)
    time.sleep(60)
