#!/usr/bin/env python

from email.message import EmailMessage
import os.path
import mimetypes
import smtplib

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

def mail():

    body = """Hey there!
I'm learning to send emails using Python!"""

    sender = 'vk@vk.com'
    recipient = 'volkan@kumbasar.net'
    body = 'lego.jpg'
    attachment_path = 'lego.jpg'

    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
    message.set_content(body)

    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
             message.add_attachment(ap.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=attachment_filename)

    print(message)
    """
    mail_server = smtplib.SMTP_SSL('smtp.example.com')
    # mail_server = smtplib.SMTP('localhost')
    mail_server.set_debuglevel(1)
    mail_server.login(sender, 'secret')
    mail_server.send_message(message)
    mail_server.quit()
    """


def generatePDF():

    fruit = {
        "elderberries": 1,
        "figs": 1,
        "apples": 2,
        "durians": 3,
        "bananas": 5,
        "cherries": 8,
        "grapes": 13
    }

    report_file = "report.pdf"

    report = SimpleDocTemplate(report_file)
    styles = getSampleStyleSheet()

    report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

    table_data = []

    for k, v in fruit.items():
        table_data.append([k, v])

    table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]

    report.build([report_title])
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

    report_pie = Pie(width=800, height=600)
    report_pie.data = []
    report_pie.labels = []
    for fruit_name in sorted(fruit):
        report_pie.data.append(fruit[fruit_name])
        report_pie.labels.append(fruit_name)

    report_chart = Drawing()
    report_chart.add(report_pie)

    report.build([report_title, report_table, report_chart])

if __name__ == "__main__":
    # mail()
    generatePDF()
