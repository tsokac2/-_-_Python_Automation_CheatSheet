import re

with open('src/urls.txt') as file:
    content = file.read()

# print(content)

pattern = re.compile("https?://(?:www.)?[^ \n]+\.com")
matches = pattern.findall(content)
print(matches)