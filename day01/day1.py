import time,re

def loadfile(file):
    c = []
    with open(file) as f:
        for line in f.readlines():
            c.append(((line[0]),int(line[1:])))
        return c

        
def solve(p,start):
    pos = start
    p1 = p2 = 0
    for dir,num_tw in p:
        if dir == 'R':
            (rot,new_pos) = divmod(pos + num_tw,100)
        if dir == 'L':
            (rot, new_pos) = divmod(pos - num_tw, 100)
        if new_pos == 0:
            p1 += 1
        if pos == 0 and rot < 0: 
            p2 += abs(rot) - 1
            pos = new_pos
            continue
        if new_pos == 0 and rot > 0:
                p2 += rot - 1
                pos = new_pos
                continue
        p2  += abs(rot)
        pos = new_pos
    return p1,p1+p2


time_start = time.perf_counter()
print(f'Solution: {solve(loadfile("day1.txt"),50)}')
print(f'Solved in {time.perf_counter() - time_start:.6f} Seconds')