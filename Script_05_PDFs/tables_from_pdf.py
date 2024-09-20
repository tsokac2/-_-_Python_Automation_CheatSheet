import tabula

table = tabula.read_pdf('src/weather.pdf', pages=1)
print(table[0])
table[0].to_csv('src/output.xlsx', index=None)