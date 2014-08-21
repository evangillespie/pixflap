
from sys import argv
from PIL import Image
from src.image_converter import ImageConverter

__author__ = ('evan', )

def convert_image(filepath):
    """
    recreate the image in the right size and with the right colours
    """
    img = Image.open(filepath)
    img = ImageConverter.prepare_image(img)
    img = ImageConverter.simplify_image(img)

    img.show()

def print_help():
    print "USAGE: %s <command>" % argv[0]
    print "COMMANDS:"
    print "convert_image <path_to_image>"

if __name__ == '__main__':
    if len(argv) >= 2:
        command = argv[1]
        if command == 'convert_image':
            if len(argv) == 3:
                convert_image(argv[2])
            else: print_help()
    else:
        print_help()