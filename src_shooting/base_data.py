import numpy as np

SX, SY = 520, 620
FS = 48

def empty_board():
    return  np.zeros((SY, SX, 3), np.uint8)