import numpy as np
from . import base_data as bd

empty_board = bd.empty_board

def sum_obj(objs):
    return sum(objs, empty_board())
    
def get_loc(fighter):
    return [int(e.mean()) for e in np.where(0 < fighter)][:2]

def is_hit(obj1, obj2, ys = (0, 300)):
    obj1 = obj1[ys[0]:ys[1],:,:]
    obj2 = obj2[ys[0]:ys[1],:,:]
    nc = lambda e: np.count_nonzero(e)
    return nc(obj1) + nc(obj2) != nc(obj1 + obj2)

def pad(a, p):
    return np.pad(a, p + ((0,0),), mode='constant', constant_values=0)


def move_x(obj, step):
    #print(step)
    if abs(step) < 2:
        return obj 
    
    if 0 < step:
        t = pad(obj, ((0,0), (step, 0)))[:, :-step, :]
    if step < 0:
        t = pad(obj, ((0,0), (0, -step)))[:, -step:, :]
        
    if t.sum() == obj.sum():
        return t
    
    return move_x(obj, step//2)

def move_y(obj, step = 50):
    if 0 < step:
        t = pad(obj, ((step, 0), (0,0)))[:-step, :,:]
    else:
        t = pad(obj, ((0, -step), (0,0)))[-step:, :,:]
    return t