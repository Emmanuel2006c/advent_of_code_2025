import time,re 

def load(file):
    with open(file) as f:
        return f.read().split('\n')

def solve(p):
    p1 = p2 = 0
    ranges, avail_ingr = [], []
    r = True
    for line in p:
        if line == '':
            r = False
            continue
        if r:
            ranges.append(list(map(int,line.split('-'))))
        else:
            avail_ingr.append(int(line))
    for ingr in avail_ingr:
        for start,end in ranges:
            if start<= ingr <= end:
                p1 += 1
                break
    e = set()
    ranges = sorted(ranges)
    nr = (0,0)
    for (s1,e1), (s2,e2) in zip(ranges,ranges[1:]):
        if e1<s2:
            p2 += e1-s1+1 + nr[1] - nr[0] + 1
        else: 
            nr = s1,e2
    mi, ma = 9999999999, -1
    summary = False
    for (s1,e1),(s2,e2) in zip(ranges,range[1:]):
        if e1 >= s2:            
            if s1 < mi:
                mi = s1
            if e2 > ma:
                ma = e2
            summary = True
        else:
            p2 += e1 - s1 +1
            if summary:
                p2 += ma - mi +1
                mi, ma = 9999999999999 + 1
            summary = True
    if summary: p2 += ma - mi+1
    return p1,p2



time_start = time.perf_counter()
print(f'Solution: {solve(load("day5.txt"))}')
print(f'Solved in {time.perf_counter() - time_start:.6f} Seconds')