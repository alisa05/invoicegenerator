import jinja2
import pdfkit
from datetime import datetime
import csv
from fpdf import FPDF, HTMLMixin
import random

def findelec ():
    with open('test_data.csv', 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 2:
                cell_data = row[3]
    return cell_data

def findename ():
    with open('test_data.csv', 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 2:
                cell_data = row[1]
    return cell_data

def date ():
    with open('test_data.csv', 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 2:
                cell_data = row[0]
    return cell_data

invoice_number = 0000
client_name = findename()
item1 = "Electricity spent"
item2 = "Price per kWh"
item3 = "Total price"
item4 = date()

subtotal1 = findelec()
subtotal2 = 0.3
total = float(subtotal1) * float(subtotal2)

today_date = datetime.today().strftime("%d %b, %Y")
month = datetime.today().strftime("%B")

context = {'invoice_number': invoice_number, 'client_name': client_name,'today_date': today_date, 'total': total, 'month': month,
           'item1': item1, 'subtotal1': subtotal1,
           'item2': item2, 'subtotal2': subtotal2,
           'item3': item3, 'item4': item4
           }

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'invoice.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
output_pdf = 'invoice.pdf'
pdfkit.from_string(output_text, output_pdf, configuration=config, css='invoice.css')