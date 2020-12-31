#!/usr/bin/env python3

import os
import requests


def getImagesList(path):
    images = []

    for (dirpath, dirnames, filenames) in os.walk(path):
        for image in filenames:

            if '.jpeg' in image:
                images.append(os.path.join(dirpath, image))

    return images


def uploadImage(url, image):
    with open(image, 'rb') as opened:
        response = requests.post(url, files={'file': opened})
        if response.ok:
            print("{} is uploaded successfully. Response result {}".format(image, response.status_code))
        else:
            print("Failure! Response code: {} text: {}".format(response.status_code, str(response.text).encode('utf-8').strip()))


if __name__ == "__main__":

    path = 'supplier-data/images'
    images = getImagesList(path)

    for image in images:
        print("Image: {}".format(image))
        uploadImage('http://localhost/upload/', image)
