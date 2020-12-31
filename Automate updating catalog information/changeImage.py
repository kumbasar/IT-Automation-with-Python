#!/usr/bin/env python3

from PIL import Image
import os


def resizeConvert(path, x=600, y=400):

    for (dirpath, dirnames, filenames) in os.walk(path):

        for image in filenames:

            if '.tiff' in image:
                # Load TIFF image
                im = Image.open(os.path.join(dirpath, image))
                new_im = im.resize((x, y)).convert("RGB")
                new_image_file = os.path.join(path, image.replace(".tiff", ".jpeg"))
                print("{} => {}".format(image, new_image_file))

                # Load Save JPEG image
                new_im.save(new_image_file, "JPEG")


if __name__ == "__main__":
    path = 'supplier-data/images'
    resizeConvert(path)
