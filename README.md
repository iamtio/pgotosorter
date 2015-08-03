# Photo organizing script
PhotoSorter is a small script in Python and Python 3 which can organize your photos. For example we have some directory:

    last_summer/
        IMG_0001.jpg
        IMG_0002.jpg
    cafe/
        IMG_0042.jpg
    Camera_2015-01-01-19-30.jpg

Script will read EXIF data from all images or file creation date(if no EXIF provided) and move them into human readable directory strucure: `Year/Year_Month/Year_Month_Day/`. For example:

    2014/
        2014_08/
            2014_08_16/
                IMG_0001.jpg
                IMG_0002.jpg
            2014_08_20/
                IMG_0042.jpg
    2015/
        2015_01/
            2015_01_01/
                Camera_2015-01-01-19-30.jpg

If names of files are identical script will not overwrite them. File will be renamed from `filename.jpg` to `filename(1).jpg`.

## Installing
Just save [`photosorter.py`](photosorter.py) and install required python libs:

    $ sudo apt-get install python-six python-pil

also you can install them from pypi. But before building `Pillow` you must install `libjpeg-dev`:

    $ sudo apt-get install libjpeg-dev
    $ pip install Pillow six

## Runing ##
Run:

    $ python photosorter.py --help

to see script arguments
