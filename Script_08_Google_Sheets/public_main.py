import pandas

url_sheet1 = "https://docs.google.com/spreadsheets/d/1cbCo3wJHtNCmpyoDYSIacQDDjbpNWHsdE9OW0MoTALQ/gviz/tq?tqx=out:csv&sheet=2023"
url_sheet2 = "https://docs.google.com/spreadsheets/d/1cbCo3wJHtNCmpyoDYSIacQDDjbpNWHsdE9OW0MoTALQ/gviz/tq?tqx=out:csv&sheet=2024"

data = pandas.read_csv(url_sheet2)

print(data)