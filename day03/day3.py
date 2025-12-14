import time, re
def loadfile(file):
    c = []
    with open(file) as f:
       for lines in f.readlines():
        c.append(lines.strip())
    return c
        
def solve(p):
    for e in p:
        digits = [int(d) for d in e]
        for d in digits:
            while(i<len(e),i=0, i++):
                curr = d[i]





time_start = time.perf_counter()
print(f'Solution {solve(loadfile('day3.txt'))}')
print(f'Thought for {time.perf_counter() - time_start:.6f} Seconds')
 