from __future__ import print_function, unicode_literals, division
import exifread
import os
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file',
                        nargs="+",
                        help="JPEG image files",
                        type=argparse.FileType('rb'))
    for f in parser.parse_args().file:
        print(get_date(f))
