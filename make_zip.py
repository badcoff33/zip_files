## Description:
##
## Recommended Python version is 2.7.X.
## Code is not compatible with Python version > V3.x.x.


__author__ = "Markus Prepens"

import os
import sys
import time
import re

try:
    # Requires Python > 2.7
    import argparse
except ImportError:
    print("Fail to import module argparse. This module is part of Python 2.7 or newer.")
    sys.exit(1)

## Create an object of the commad line options reader.
parser = argparse.ArgumentParser(description='Create a ZIP archive. The list of \
    files is read from command line parameter.')

parser.add_argument('--files', '-f', nargs='+',
                    help='at least one file')

parser.add_argument('--verbose', '-v',
                    help='be verbose',
                    action='store_true')

## Get the acual command line options.
args = parser.parse_args()
print(args)

if args.verbose == True:
    print("be verbose")

for file in args.files:
    if os.path.isfile(file):
        print("file exists")
    else:
        print("file does not exists")
        exit(-1)


