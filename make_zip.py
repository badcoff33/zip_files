## Description:
##
## Recommended Python version is 2.7.X.
## Code is not compatible with Python version > V3.x.x.


__author__ = "Markus Prepens"

import os
import sys
import shutil

try:
    # Requires Python > 2.7
    import argparse
except ImportError:

    print("Fail to import module argparse. This module is part of Python 2.7 or newer.")
    sys.exit(1)

def cleanup(thisFiles):
    if os.path.isfile(thisFile):
        os.remove(thisFile)

class ZipArchiver():
    """This is a class to make a release package in form of a ZIP archive.
        Class does not require the zipfile package. It uses the shutil package."""
    def __init__(self, outfile):
        self.list_of_files = []
        self.outfile = outfile

    def add_file(self, new_file):
        if os.path.isfile(new_file):
            self.list_of_files.append(new_file)

    def create_zip(self, releaseName):
        shutil.rmtree(releaseName, True) # ignore errors
        os.mkdir(releaseName)
        for src in self.list_of_files:
            target = releaseName + os.sep + os.path.basename(src)
            shutil.copyfile(src, target)
        shutil.make_archive(self.outfile, "zip", ".", releaseName)


## Create an object of the commad line options reader.
parser = argparse.ArgumentParser(description='Create a ZIP archive. The list of \
    files is read from command line parameter.')

parser.add_argument('--files', '-f', nargs='+',
                    help='at least one file')

parser.add_argument('--output', '-o', nargs='?',
                    help='file of the ZIP archive')

parser.add_argument('--release', '-r', nargs='?',
                    help='name of release')

parser.add_argument('--verbose', '-v',
                    help='be verbose',
                    action='store_true')

## Get the acual command line options.
args = parser.parse_args()

myZip = ZipArchiver(args.output)
for file in args.files:
    myZip.add_file(file)
myZip.create_zip(args.release)
