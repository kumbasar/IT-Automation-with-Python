#!/usr/bin/env python

import subprocess
import os
from multiprocessing import Pool

src = "data/prod/"
dest = "data/prod_backup/"


def run(src_dir):
    # Set dest_dir
    dest_dir = src_dir.replace('./'+src_dir, dest)
    print("Backup src: {} to dest: {}".format(src_dir, dest_dir))

    # Call rsync
    subprocess.call(["rsync", "-arq", src_dir, dest_dir])


if __name__ == "__main__":
    tasks = []
    for root, dirs, files in os.walk("./"+src, topdown=False):
        for name in dirs:
            tasks.append(os.path.join(root, name))

    # Create a pool of specific number of CPUs
    pool = Pool(len(tasks))

    # Start each task within the pool
    pool.map(run, tasks)
