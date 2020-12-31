#!/usr/bin/env python3

import os
import requests
import re


def uploadDescription(url, description):
    """
    Post feedback to server
    """
    response = requests.post(url, json=description)

    if response.status_code == 201:
        print("Feedbacks are posted successfully. Response code: {}".format(response.status_code))
    else:
        print("Failure! Response code: {} text: {}".format(response.status_code, str(response.text).encode('utf-8').strip()))


def getDescriptions(path):
    """
    Get all description from path
    """
    description_list = []

    for (dirpath, dirnames, filenames) in os.walk(path):
        for fn in filenames:
            with open(os.path.join(dirpath, fn), mode='r', encoding="utf-8") as fn_file:
                lines = fn_file.readlines()
                # skip file if field are missing
                if len(lines) < 3:
                    continue

                # Get weight value
                m = re.match(r"^(\w+)", lines[1].strip())

                description_list.append({
                    "name": lines[0].strip(),
                    "weight": int(m.group(1)),
                    "description": "".join(lines[2:]).strip(),
                    "image_name": fn.replace(".txt", ".jpeg")
                })

    return description_list


if __name__ == "__main__":
    descriptions = getDescriptions('supplier-data/descriptions')

    for description in descriptions:
        print("Fruit description: {}".format(description))
        uploadDescription('http://localhost/fruits/', description)
