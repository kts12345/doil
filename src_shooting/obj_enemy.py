from PIL import Image
import numpy as np
from . import base_data as bd
from . import base_algorithm as ba

FS = bd.FS
SX, SY = bd.SX, bd.SY
PATH_LEVEL_01 = './images/enemy_level_01.jpg'
pad = ba.pad

def make_enemy(pos_x = 300):
    sz_x, sz_y = FS*3//4, FS*3//8
    obj = Image.open(PATH_LEVEL_01).resize((sz_x, sz_y))
    obj = np.array(obj)
    obj = pad(obj, ((50, SY-50-sz_y), (pos_x, SX-pos_x-sz_x)))
    
    return obj 


def make_enemies(count = 2):
    es = [make_enemy(50*i) for i in range(count)]
    es += [make_enemy(SX - 50 - 150 - 50*i) for i in range(count)]
    return es