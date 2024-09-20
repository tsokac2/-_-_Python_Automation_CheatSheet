import gspread
import statistics

gc = gspread.service_account('secrets.json') # You need to create a new project on the 'https://console.cloud.google.com/welcome?project=automate-with-python-433711'
spreadsheet = gc.open('private_data') # Name of the spreadsheet on the Google Drive
# Get a worksheet by name
worksheet1 = spreadsheet.worksheet('2024')

# Update a cell
# worksheet1.update('B5', -29)

# Update a cell based on row-column
# worksheet1.update_cell(5, 5, -39)

existing_column = worksheet1.get_values('E2:E25')
new_column = [[round((float(i[0])) * 9/5 + 32)]  for i in existing_column]
print(new_column)

worksheet1.update('F2:E25', ['Fahrenheit'] + new_column)

# Calculate avarage and add to Worksheet
avarage = statistics.mean(existing_column)
worksheet1.update('G1', avarage)



