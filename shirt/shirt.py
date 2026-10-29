import sys
from PIL import Image
import PIL
import os

try:
    if sys.argv[1].endswith('.jpg'.casefold()) or sys.argv[1].endswith('.jpeg'.casefold()) or sys.argv[1].endswith('.png'.casefold()):
        f1n, f1ext = os.path.splitext(sys.argv[1])
        f2n, f2ext = os.path.splitext(sys.argv[2])
        if f1ext==f2ext: 
            if len(sys.argv)>3:
                sys.exit('too many arguments')
            try:
                shirt = Image.open('shirt.png')
                face = Image.open(sys.argv[1])
                face = face.resize(shirt.size)
                face_size = face.size
                face.paste(shirt, box=(0,0), mask=shirt)
                face.save(sys.argv[2])
            except FileNotFoundError:
                sys.exit(f'could not read file {sys.argv[1]}')
        else:
            sys.exit('two files do not have the same extension')
    else:
        sys.exit('not a csv file')
except IndexError:
    if len(sys.argv)>3:
        sys.exit('too many arguments')
    else:
        sys.exit('too few arguments')