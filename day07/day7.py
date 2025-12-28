import time,re 

def loadfile(file):
    with open(file) as f:
        lines = f.readlines()
    return numbers,operators

def solve(p):
    return p

time_start = time.perf_counter()
print(f"Solution: {solve(loadfile('day7.txt'))}")
print(f"Thought for {time.perf_counter() - time_start:.6f} Seconds")