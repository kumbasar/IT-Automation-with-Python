#!/usr/bin/env python3

import re
import sys
import operator
import csv


def parse_syslog(syslog_file):

    per_user = {}
    error = {}
    pattern = r"(ERROR|INFO)\s(.*)\((.*)\)"

    """Open sysfile file"""
    with open(syslog_file, mode='r', encoding='UTF-8') as logs:
        for log in logs.readlines():
            result = re.search(pattern, log.strip())
            message_type = result.group(1).strip()
            message = result.group(2).strip()
            user = result.group(3).strip()

            """Update Error dictionary"""
            if message_type.upper() == "ERROR":
                if message in error:
                    error[message] += 1
                else:
                    error[message] = 1

            """Update User Dictionary"""
            if user in per_user:
                per_user[user][message_type] += 1
            else:
                if message_type == 'INFO':
                    per_user[user] = {'INFO': 1, 'ERROR': 0}
                # It have to be an ERROR message
                else:
                    per_user[user] = {'INFO': 0, 'ERROR': 1}
        sorted_per_user = {k: per_user[k] for k in sorted(per_user.keys())}
        sorted_error = {k: v for k, v in sorted(error.items(), key=lambda item: item[1], reverse=True)}

    return sorted_per_user, sorted_error


def generate_csv_reports(per_user, error):
    """Create Error report"""
    with open("error_message.csv", "w") as error_csv:
        writer = csv.writer(error_csv)
        writer.writerow(["Error", "Count"])
        for error, count in error.items():
            writer.writerow([error, count])

    """Create User report"""
    with open("user_statistics.csv", "w") as user_csv:
        writer = csv.writer(user_csv)
        writer.writerow(["Username", "INFO", "ERROR"])
        for user, count in per_user.items():
            writer.writerow([user, str(count['INFO']), str(count['ERROR'])])


def main():
    csv_file_location = "syslog.log"

    if len(sys.argv) == 2:
        csv_file_location = sys.argv[1]

    per_user, error = parse_syslog(csv_file_location)
    generate_csv_reports(per_user, error)


if __name__ == "__main__":
    main()
