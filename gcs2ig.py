#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This script downloads the most recent image from Google Cloud Storage and uploads its to Instagram, 
using part of its metadata as text associated with the image.
"""
import argparse

__author__ = "Jorge Arévalo"
__copyright__ = "Copyright 2020, Jorge Arévalo"
__credits__ = ["Jorge Arévalo"]
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "Jorge Arévalo"
__email__ = "jorgeas80@tuta.io"
__status__ = "Development"

parser = argparse.ArgumentParser(description='Downloads most recent image from GCS and uploads it to IG')

# Positional Arguments
parser.add_argument('argument_name',
                    help="argument description",
                    nargs='?',
                    const=0)

# Optional Arguments
parser.add_argument("-f", "--foo",
                    help="specify foo",
                    action='store_true')
parser.add_argument("-b", "--bar",
                    help="specify bar",
                    metavar='BAR',
                    nargs=1)

args = parser.parse_args()


def main():
    if args.foo:
        print("foo")
    if args.argument_name:
        print("Argument name: %s" % args.argument_name)
    if args.bar:
        print("Specified bar: %s" % args.bar)

if __name__ == '__main__':
    main()