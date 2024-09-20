import fitz

# with fitz.open('src/students.pdf') as pdf:
#     for page in pdf:
#         print(20*'-')
#         print(page.get_text())


with fitz.open('src/students.pdf') as pdf:
    text = ''
    for page in pdf:
        text = text + page.get_text()
        print(text)