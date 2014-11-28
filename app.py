from __future__ import print_function, unicode_literals, division
import exifread
import os
import glob
import sys
import argparse
from datetime import datetime


def get_file_date(input_file):
    """
    Get file creation date
    """
    try:
        date = str(exifread.process_file(input_file)['Image DateTime'])
        date = datetime.strptime(date, "%Y:%m:%d %H:%M:%S")
    except KeyError:
        msg = "Warning! EXIF tag not found"\
              "for file '{0}'".format(input_file.name)
        print(msg, file=sys.stderr)
        date = datetime.fromtimestamp(os.path.getctime(input_file.name))
    return date


def find_files(directory, filter, recursive):
    """Filter files in directory"""
    dirs = [directory]
    if recursive:
        dirs = (d[0] for d in os.walk(directory))
    for dir in dirs:
        for file in glob.iglob(os.path.join(dir.decode('utf-8'), filter)):
            yield file


def move_file(filename, date, directory):
    df = date.strftime
    new_file = os.path.join(directory,
                            df("%Y"),
                            df("%Y_%m"),
                            df("%Y_%m_%d"),
                            os.path.split(filename)[-1])
    date = date.strftime("%Y-%m-%d")
    print(os.path.abspath(filename))
    print(os.path.abspath(new_file))


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
    args = vars(parser.parse_args())
    for file_name in find_files(**args):
        with open(file_name, 'rb') as file:
            date = get_file_date(file)
        move_file(file_name, date, args['directory'])

