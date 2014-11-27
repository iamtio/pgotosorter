import exifread
import sys
import os
import argparse
from datetime import datetime


def get_date(input_file):
    try:
        date = str(exifread.process_file(input_file)['Image DateTime'])
        date = datetime.strptime(date, "%Y:%m:%d %H:%M:%S")
    except KeyError:
        date = datetime.fromtimestamp(os.path.getctime(input_file.name))
    return date.strftime("%Y-%m-%d")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(name='-f',
                        help="JPEG image file",
                        type=argparse.FileType('rb'),
                        required=True)
    args = parser.parse_args()
    print get_date(args.f)
