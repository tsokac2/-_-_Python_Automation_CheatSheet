import re

with open('src/ips.txt') as file:
    content = file.read()

print(content)

pattern = re.compile("[0-9]{3}\.[0-9]{3}\.12[0-9]{1}\.[0-9]{3}")
matches = pattern.findall(content)
print(matches)