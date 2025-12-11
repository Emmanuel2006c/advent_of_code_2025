import time, re
def loadfile(file):
    with open(file) as f:
        s = f.read().replace('-' , ',').split(',')
        n = [int(x) for x in s]
        idrange = {n[i] : n[i+1] for i in range(0,len(n),2)}
        return idrange
        
       
    
def solve(ranges):
    p1 = 0
    for start,end in ranges.items():
#print(f'Start:{start} - End:{end}') 
        for wert in range(start,end+1): 
            w = str(wert) 
            l = len(w) 
            if l % 2 == 1: continue 
            h = l // 2 
            if w[:h] == w[h:]: 
                p1+= wert 
    return p1



time_start = time.perf_counter()
print(f'Solution {solve(loadfile('day2.txt'))}')
print(f'Thought for {time.perf_counter() - time_start:.6f} Seconds')
 