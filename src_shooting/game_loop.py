import numpy as np
import random
from PIL import Image
from . import base_data as bd
from . import base_algorithm as ba
from IPython.display import display

from src_shooting.base_algorithm \
    import (pad, is_hit, get_loc, move_x, move_y, sum_obj)

from src_shooting.obj_bullet \
    import (make_bullet, make_bullet_e, bullet_step, bullet_step_e, 
            FS, SX, SY)

from src_shooting.base_keyboard import get_step_

from src_shooting.base_ipython import show
from src_shooting.obj_fighter import (make_fighter, make_crash_mark)
from src_shooting.obj_enemy import (make_enemies)

es = make_enemies(3) 
my_fighter = make_fighter()
print(my_fighter.shape)
#show(my_fighter)
#show(sum_obj(es))

FS = bd.FS
SX, SY = bd.SX, bd.SY
PATH_FIGHTER = './images/my_fighter.jpg'
PATH_CRASH_MARK = './images/crash.jpg'
pad = ba.pad

import IPython.display as ipd
import time


def get_step():
    return get_step_()
        
def game_loop():
    mf = my_fighter.copy()
    
    bs = []
    bs_e = []
    es = []
    max_bs = 3
    last_bs_time = 0
    last_bs_time_e = -3
    between_bs_time = 1.2 
    between_bs_time_e = 0.4 
    i  = 0
    end_game_count = 0
    power_bullet = False
    stage = -1 
    while True:
        i += 1
        if between_bs_time < (time.time() - last_bs_time):
            loc = get_loc(mf)
            b = make_bullet(loc[1]-25, stage)
            bs.append(b)
            last_bs_time = time.time()
        
            
        if between_bs_time_e < (time.time() - last_bs_time_e) \
            and 0 < len(es): 
            last_bs_time_e = time.time()
            if  random.randint(0, max(2, 7 - stage)) == 0:
                enemy = random.choice(es)
                
                loc = get_loc(enemy)
                b = make_bullet_e(loc[::-1])
                bs_e.append(b)
            
        step  = get_step()
        if step is None:
            break
        mf = move_x(mf, step)
        sum_b = sum(bs, np.zeros_like(mf))
        sum_b_e = sum(bs_e, np.zeros_like(mf))
        
        e_step = min(stage+2, 4)
        es = [move_x(e, -e_step if (i//41)%2 else e_step) for e in es]
        
        if i%160 == 1 and 160 < i:
            if (i // 320) % 2:
                ys = -50
            else:
                ys = 50
            es = [move_y(e, ys) for e in es]
        
        es = [e for e in es if not is_hit(sum_b, e)] 
        
        scene =  sum([mf, sum_b, sum_b_e] + es, np.zeros_like(mf))
        if is_hit(sum_b_e, mf, (SY-100, SY)):
            show(scene + make_crash_mark(mf))
            break
        show(scene)
        
        new_bs = []
        for b in bs:
            b = bullet_step(b, stage)
            if b is not None:
                new_bs.append(b)
        bs = new_bs
                
        new_bs_e = []
        for b in bs_e:
            b = bullet_step_e(b, stage)
            if b is not None:
                new_bs_e.append(b)
        bs_e = new_bs_e
                
        if len(es) == 0:
            bs_e = []
            end_game_count += 1
            if 0 < stage:
                power_bullet = True
            if 2 < stage:
                between_bs_time = 0.5
            
            
        if  end_game_count == 40:
            end_game_count = 0
            stage += 1
            es = make_enemies(min(stage+1, 3))
            i = 0
        
        time.sleep(0.03)
        ipd.clear_output(wait=True)
        
def start():
    while True:
        try:
            game_loop()
        except:
            break
        time.sleep(5)