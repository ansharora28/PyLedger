import jinja2
import pdfkit
import os
from datetime import datetime

# Get input from the user
client_name = input("Enter client name: ")

# Get the number of items from the user
num_items = int(input("Enter number of items: "))

# Initialize empty lists to store item details
items = []
subtotals = []

# Use a loop to collect information for each item
for i in range(num_items):
    item_name = input(f"Enter item {i + 1} name: ")
    item_subtotal = float(input(f"Enter subtotal for item {i + 1}: "))
    
    items.append(item_name)
    subtotals.append(item_subtotal)

# Calculate the total
total = sum(subtotals)

today_date = datetime.today().strftime("%d %b, %Y")
month = datetime.today().strftime("%B")

# Create context dictionary dynamically
context = {'client_name': client_name, 'today_date': today_date, 'total': f'Rs{total:.2f}'}

for i in range(num_items):
    context[f'item{i + 1}'] = items[i]
    context[f'subtotal{i + 1}'] = f'{subtotals[i]:.2f}'

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'template.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

output_pdf = 'invoice.pdf'
output_pdf_path = os.path.join('../invoices', 'invoice.pdf')

pdfkit.from_string(output_text, output_pdf_path, configuration=config, css='style.css')
