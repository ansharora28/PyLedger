import jinja2
import pdfkit
import os
from datetime import datetime

client_name = "Client Name"
item1 = "item 1"
item2 = "item 2"
item3 = "item 3"

subtotal1 = 499
subtotal2 = 399
subtotal3 = 129
total = subtotal1 + subtotal2 + subtotal3

today_date = datetime.today().strftime("%d %b, %Y")
month = datetime.today().strftime("%B")

context = {'client_name': client_name, 'today_date': today_date, 'total': f'Rs{total:.2f}',
           'item1': item1, 'subtotal1': f'{subtotal1:.2f}',
           'item2': item2, 'subtotal2': f'{subtotal2:.2f}',
           'item3': item3, 'subtotal3': f'{subtotal3:.2f}'
           }

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'template.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
output_pdf = 'invoice.pdf'
output_pdf_path = os.path.join('../invoices', 'invoice.pdf')

pdfkit.from_string(output_text, output_pdf_path, configuration=config, css='style.css')