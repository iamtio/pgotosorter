import exifread
import sys

class Image(object):
    def __init__(self, filename):
        self.file = open(filename, 'rb')

    def __del__(self):
        self.file.close()

    def get_date(self):
        return exifread.process_file(self.file)['Image DateTime']

if __name__ == "__main__":
    img = Image(sys.argv[1])
    print img.get_date()
