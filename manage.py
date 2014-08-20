
from sys import argv

from src.image_converter import ImageConverter

__author__ = ('evan', )

def convert_image(filepath):
    """
    recreate the image in the right size and with the right colours
    """
    ic = ImageConverter()
    print ic.convert_image(filepath)

def print_help():
    print "USAGE: %s <command>" % argv[0]
    print "COMMANDS:"
    print "convert_image <path_to_image>"

if __name__ == '__main__':
    if len(argv) >= 2:
        command = argv[1]
        if command == 'convert_image':
            if len(argv) == 3:
                prepare_image(argv[2])
            else: print_help()
    else:
        print_help()