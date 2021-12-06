from PIL import Image
import numpy as np
from . import base_data as bd
from . import base_algorithm as ba

FS = bd.FS
SX, SY = bd.SX, bd.SY
PATH_FIGHTER = './images/my_fighter.jpg'
PATH_CRASH_MARK = './images/crash.jpg'
pad = ba.pad
get_loc = ba.get_loc

def make_fighter():
    obj = Image.open(PATH_FIGHTER).resize((FS, FS))
    obj = np.array(obj)
    obj = pad(obj, ((SY-30-FS, 30), ((SX-FS)//2, (SX-FS)//2)))
    return obj 

def make_crash_mark(mf):
    y, x = get_loc(mf)
    t = Image.open(PATH_CRASH_MARK)
    t = t.resize((FS, FS))
    t = np.array(t)
    obj = np.zeros((SY, SX, 3), np.uint8)
    obj[y-FS//2:y+FS//2, x-FS//2:x+FS//2] = t
    return obj
