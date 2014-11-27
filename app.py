import exifread
import os
import argparse
from datetime import datetime
import warnings


def get_date(input_file):
    """
    Get file creation date
    """
    try:
        date = str(exifread.process_file(input_file)['Image DateTime'])
        date = datetime.strptime(date, "%Y:%m:%d %H:%M:%S")
    except KeyError as e:
        warnings.warn("EXIF tag not found: {0}".format(e))
        date = datetime.fromtimestamp(os.path.getctime(input_file.name))
    return date.strftime("%Y-%m-%d")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',
                        help="JPEG image file",
                        type=argparse.FileType('rb'),
                        required=True)
    args = parser.parse_args()
    print get_date(args.f)
