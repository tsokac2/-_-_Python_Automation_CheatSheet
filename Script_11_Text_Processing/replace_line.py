with open('merged.csv', 'r') as file:
    content = file.readlines()

content[0] = 'ID,AMOUNT,COST'

with open('merged.csv', 'w') as file:
    file.writelines(content)