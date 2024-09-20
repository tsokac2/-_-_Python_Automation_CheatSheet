with open('src/file3.csv', 'r') as file:
    content = file.read()


modified_content = (content[:-3])

with open('src/file4.csv', 'w') as file:
    file.write(modified_content)