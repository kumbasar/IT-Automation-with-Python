#!/usr/bin/env python3

import os
import requests


def postFeedback(url, feedback):
    """
    Post feedback to server
    """
    response = requests.post(url, json=feedback)

    if response.status_code == 201:
        print("Feedbacks are posted successfully. Response code: {}".format(response.status_code))
    else:
        print("Failure! Response code: {} text: {}".format(response.status_code, str(response.text).encode('utf-8').strip()))


def getFeedback(path):
    """
    Get all feedbacks from path
    """
    feedback_list = []

    for (dirpath, dirnames, filenames) in os.walk(path):
        for file in filenames:
            with open(os.path.join(dirpath, file), mode='r', encoding="utf-8") as feedback_file:
                lines = feedback_file.readlines()

                # skip file if field are missing
                if len(lines) < 4:
                    continue

                feedback_list.append({
                    "title": lines[0].strip(),
                    "name": lines[1].strip(),
                    "date": lines[2].strip(),
                    "feedback": "".join(lines[3:]).strip()
                })

    return feedback_list


if __name__ == "__main__":
    feedbacks = getFeedback('/data/feedback')

    for feedback in feedbacks:
        print("Feedback: {}".format(feedback))
        postFeedback('http://35.184.218.190/feedback/', feedback)
