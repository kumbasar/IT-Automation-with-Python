#!/usr/bin/env python3

from PIL import Image
import os


def rotateResizeConvert(path, output, x=128, y=128, rotate=-90):

    for (dirpath, dirnames, filenames) in os.walk(path):

        for image in filenames:

            # Skip hidden files
            if '.' == image[0]:
                continue

            # Load TIFF image
            im = Image.open(os.path.join(dirpath, image))
            new_im = im.rotate(rotate).resize((x, y)).convert("RGB")
            new_image_file = os.path.join(output, image)
            print("{} => {}".format(image, new_image_file))

            # Load Save JPEG image
            new_im.save(new_image_file, "JPEG")


if __name__ == "__main__":
    source = 'images'
    output = '/opt/icons'
    rotateResizeConvert(source, output)
