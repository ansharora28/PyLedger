import jinja2
import pdfkit
import os
from datetime import datetime

# Get input from the user
company_name = input("Enter your company name: ")
company_address_line1 = input("Enter your company address (line 1): ")
company_address_line2 = input("Enter your company address (line 2): ")
company_phone_number = input("Enter your company phone number: ")
company_email = input("Enter your company email: ")

client_name = input("Enter client name: ")

# Get client account details
account_holder_name = input("Enter client's account holder name: ")
bank_name = input("Enter client's bank name: ")
account_number = input("Enter client's account number: ")
ifsc_code = input("Enter client's IFSC code: ")

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

# Get additional information
today_date = datetime.today().strftime("%d %b, %Y")
month = datetime.today().strftime("%B")

# Create context dictionary dynamically
context = {
    'company_name': company_name,
    'company_address_line1': company_address_line1,
    'company_address_line2': company_address_line2,
    'company_phone_number': company_phone_number,
    'company_email': company_email,
    'client_name': client_name,
    'today_date': today_date,
    'total': f'Rs{sum(subtotals):.2f}',
    'account_holder_name': account_holder_name,
    'bank_name': bank_name,
    'account_number': account_number,
    'ifsc_code': ifsc_code,
}

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
