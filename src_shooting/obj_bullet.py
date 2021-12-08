import numpy as np
from . import base_data as bd
from . import base_algorithm as ba

SX, SY = bd.SX, bd.SY
FS = bd.FS
empty_board = bd.empty_board
pad = ba.pad

def make_bullet(x, stage):
    if stage < 1:
        power = False
        y_len = 30
    if stage == 1:
        power = False
        y_len = 60
    if stage == 2:
        power = True
        y_len = 30
    if stage >= 3:
        power = True
        y_len = 60
        
    bullet = empty_board()
    
    y = SY - 50 - FS  
    base_x = x + 8 
    color = [100,100,0]
    
    x = base_x
    bullet[y-y_len:y, x:x+2] = color
    
    x = base_x + 32 
    bullet[y-y_len:y, x:x+2] = color
    
    if power:
        #x = org_x + 20 
        #bullet[y-32:y-7, x:x+3] = [0,255,0]
        
        x = base_x + 17 
        bullet[y-y_len-10:y-10, x:x+2] = color
        
        #x = org_x + 60 
        #bullet[y-32:y-7, x:x+3] = [0,255,0]
    
    return bullet

def make_bullet_e(xy, step):
    bullet = np.zeros((SY, SX, 3), np.uint8)
    color = np.array([120, 0, 120])
        
    x, y = xy
    bullet[y+45:y+50, x-1:x+1] = color*2
    bullet[y+40:y+45, x-3:x+3] = color
    bullet[y+35:y+40, x-4:x+4] = color/2
    bullet[y+30:y+35, x-6:x+6] = color/3
    return bullet
    

def bullet_step(bullet, stage):
    if stage < 2:
        step = 30
    elif stage < 3:
        step = 50
    else:
        step = 70
    nb = pad(bullet, ((0,step), (0,0)))[step:,:,:]
    if nb.sum() == 0:
        return None
    return nb

def bullet_step_e(bullet, stage):
    if stage < 2:
        step = 3
    elif stage < 3:
        step = 4
    elif stage < 4:
        step = 5
    else:
        step = 7
    nb =  pad(bullet, ((step,0), (0,0)))[:-step,:,:]
    if nb.sum() == 0:
        return None
    return nb