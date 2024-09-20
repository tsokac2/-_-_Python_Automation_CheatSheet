import gspread
import re

gc = gspread.service_account('secrets.json') # You need to create a new project on the 'https://console.cloud.google.com/welcome?project=automate-with-python-433711'
spreadsheet = gc.open('private_data') # Name of the spreadsheet on the Google Drive

# Get a worksheet by index
# worksheet1 = spreadsheet.get_worksheet(0)

# Get a worksheet by name
worksheet1 = spreadsheet.worksheet('2024')

#data = worksheet1.get_all_records()
#print(data[10])

#Get a row of rows by cells
# data = worksheet1.get_values('A5:E5')
# print(data)


#Get a row of rows by index
# data = worksheet1.row_values(3)
# print(data)

#Get a column
# column = worksheet1.col_values(2)
# print(column)

# Get cell using acell
# cell2 = worksheet1.acell('D5').value
# print(cell2)

# Search for a cell
# cell3 = worksheet1.find('-10')
# print(cell3.row, cell3.col)

# Search for many cells
# cells = worksheet1.find('-9')
# print(cells)

# Search for partial matches
# reg = re.compile(r'99')
# cells = worksheet1.findall(reg)
# for cell in cells:
#     print(cell.row, cell.col)