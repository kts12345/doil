import time

def get_step_():
    with open('key.txt') as f:
        lines = f.read().splitlines()
    if len(lines) != 2:
        return 0
    
    t = float(lines[0])
    c = lines[1]
    if 0.7 < (time.time() - t):
        return 0
    if c in 'dDㅇ':
        return 12
    if c in 'aAㅁ':
        return -12
    if c in 'qQㅂㅃ': 
        return None 
    return 0