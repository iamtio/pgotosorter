from __future__ import print_function, unicode_literals, division
import exifread
import os
import glob
import sys
import argparse
from datetime import datetime


def get_date(input_file):
    """
    Get file creation date
    """
    try:
        date = str(exifread.process_file(input_file)['Image DateTime'])
        date = datetime.strptime(date, "%Y:%m:%d %H:%M:%S")
    except KeyError:
        msg = "Warning! File '{0}': EXIF tag not found".format(input_file.name)
        print(msg, file=sys.stderr)
        date = datetime.fromtimestamp(os.path.getctime(input_file.name))
    return date.strftime("%Y-%m-%d")


def find_files(directory, filter, recursive):
    """Filter files in directory"""
    dirs = [directory]
    if recursive:
        dirs = (d[0] for d in os.walk(directory))
    for dir in dirs:
        for file in glob.iglob(os.path.join(dir.decode('utf-8'), filter)):
            yield file

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', '-d',
                        metavar="DIR",
                        help="Directory to scan files",
                        required=True)
    parser.add_argument('--recursive', '-r',
                        help="Find files in subdirs",
                        action="store_true")
    parser.add_argument('--filter', '-f',
                        metavar="GLOB",
                        help="Filter files. Default: '*.jpg'",
                        default="*.jpg")

    for file_name in find_files(**vars(parser.parse_args())):
        with open(file_name, 'rb') as f:
            print(get_date(f))
