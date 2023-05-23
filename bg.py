# A basic background changer in python

import ctypes
import sys
import os

if len(sys.argv) < 2:
    print('Usage: py bg.py [image name]')
    sys.exit()

imageName = sys.argv[1] + ".png"

WALLPAPER_PATH = "C:\\Users\\Jordan\\backgrounds\\" + imageName
exists = os.path.isfile(WALLPAPER_PATH)

if exists:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, 3)
else:
    print("File does not exist.")
