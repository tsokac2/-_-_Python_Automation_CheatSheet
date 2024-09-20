import gspread
import time

# Establish connection - You need to create a new project on the 'https://console.cloud.google.com/welcome?project=automate-with-python-433711
gc = gspread.service_account('secrets.json')

# Get spreadsheet - Name of the spreadsheet on the Google Drive
spreadsheet = gc.open('private_data')

# Get a worksheet
worksheet1 = spreadsheet.worksheet('2024')
worksheet2 = spreadsheet.worksheet('2025')

while True:
    value1 = worksheet1.acell('F1').value
    time.sleep(2)
    value2 = worksheet1.acell('F1').value
    if value1 != value2:
        worksheet2.update("A1", 'CHANGED')


