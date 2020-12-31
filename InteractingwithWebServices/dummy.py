#!/usr/bin/env python3

import json
import csv
import yaml
import requests


def get_csv(csv_file):

    csv_list = []

    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row)
            csv_list.append(row)

    return csv_list


def to_json_file(list, file):
    with open(file, mode='w') as file_json:
        json.dump(list, file_json, indent=2)


def to_yaml_file(list, file):
    with open(file, mode='w') as file_yaml:
        yaml.safe_dump(list, file_yaml)


def post(url):
    response = requests.get(url)

    print('Response code: {}'.format(response.status_code))
    print('Response body: {}'.format(response.text[:300]))
    print('Response Accept-Encoding header: {}'.format(response.request.headers['Accept-Encoding']))

    response.raise_for_status()


if __name__ == "__main__":
    people = get_csv('people.csv')
    to_json_file(people, 'people.json')
    to_yaml_file(people, 'people.yaml')

    post('https://www.google.com')
