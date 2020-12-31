#!/usr/bin/env python3

import reports
import os
import datetime
import emails


def getDescriptions(path):
    """
    Get all description from path
    """
    description = ""

    for (dirpath, dirnames, filenames) in os.walk(path):
        for fn in filenames:
            with open(os.path.join(dirpath, fn), mode='r', encoding="utf-8") as fn_file:
                lines = fn_file.readlines()
                # skip file if field are missing
                if len(lines) < 3:
                    continue

                description += "<br/>name: {}<br/>weight: {}<br/>".format(lines[0].strip(), lines[1].strip())

    return description


if __name__ == "__main__":

    today = datetime.datetime.today()

    path = 'supplier-data/descriptions'

    attachment = '/tmp/processed.pdf'
    title = "Processed Update on {}".format(today.strftime("%d/%m/%Y"))
    paragraph = getDescriptions(path)

    reports.generate_report(attachment, title, paragraph)

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate(sender, receiver, subject, body, attachment)
    emails.send(message)
