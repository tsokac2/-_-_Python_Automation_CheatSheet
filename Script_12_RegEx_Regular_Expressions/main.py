import re

text = "Hi team. I am part of API integration Team zero_tom@email.com, need a admin access to troubleshoot admin@airbnbcoworker.com partner cases and issues. Thank you."

pattern = re.compile("[^ ]+@[^ ]+.[a-z]+") # Email pattern
matches = pattern.findall(text)
print(matches)