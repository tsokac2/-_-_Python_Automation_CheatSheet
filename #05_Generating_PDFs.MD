<h1 align="center">Generating PDFs | Extracting Data from PDFs</h1>

### Overview of the Section
* **[Creating a PDF Document with Python](#creating-pdf)**
* **[Generating a PDF from Excel Spreadsheets](#excel-pdf)**

#
### <a name="creating-pdf">Creating a PDF Document with Python</a>

The fpdf library offers various methods for formatting and styling the PDF content.
This is a basic example, and you can explore the library documentation for more functionalities.

#### 1. Create an FPDF Object:
```
from fpdf import FPDF

# Create an FPDF object with options
pdf = FPDF(orientation='P', unit='pt', format='A4')  # adjust options as needed
```
#### 2. Add a Page:

```pdf.add_page()```

#### 3. Add an Image:
``pdf.image(path_to_image, width, height)  # adjust width and height as needed
``
#### 4. Add Text: 
```
pdf.set_font(family='Times', style='B', size=24)  # set font options
pdf.cell(w=0, h=50, txt='Malayan Tiger', ln=1, align='C')  # add text with 
```
* ``w``: width of the cell (0 for full width)
* ``h``: height of the cell
* ``txt``: text to be added
* ``ln``: 1 for a line break after the cell
* ``align``: alignment (C for center)

#### 5. Add Multi-line Text:
```
pdf.set_font(family='Times', size=12)
pdf.multi_cell(w=0, h=50, txt=long_text)  # use multi_cell for multi-line text
```
#### 6. Save the PDF:
```pdf.output('output.pdf')  # save the PDF with a filename```

**[Back To The Top](#Overview-of-the-Section)**
#
### <a name="excel-pdf">Generating a PDF from Excel Spreadsheets</a>

This process involves loading data from an Excel file, iterating through each row, and dynamically generating a PDF file for each row using the FPDF library. 

The code includes steps to automate the content generation for each PDF, making it efficient and reducing redundancy. 

The process also allows for the easy handling of CSV files by simply changing the file reading method.

#### 1. Load Excel data into a DataFrame using pandas
``import pandas as pd
df = pd.read_excel('data.xlsx')``

#### 2. Install necessary packages
``pip install openpyxl fpdf pandas``

#### 3. Iterating Over Data:
``` 
for index, row in df.iterrows():
    # Access row data by column name
    name = row['Name']
    kingdom = row['Kingdom']
```
#### 4. Generating PDF Files:
Import and create an instance of FPDF:
``` 
from fpdf import FPDF
pdf = FPDF(orientation='P', unit='pt', format='A4')
``` 
For each row, create a new PDF file:
``` 
for index, row in df.iterrows():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=24)
    pdf.cell(200, 10, txt=row['Name'], ln=True)
    # Additional content can be added here
``` 
#### 5. Adding Data to PDFs:
Dynamically add row data to the PDF:
``` 
for column in df.columns[1:]:
        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt=f'{column.title()}:')
``` 

#### 6. Saving the PDF:
Save the generated PDF with a dynamic file name:
``pdf.output(f"{row['Name']}.pdf")`` 

**[Back To The Top](#Overview-of-the-Section)**