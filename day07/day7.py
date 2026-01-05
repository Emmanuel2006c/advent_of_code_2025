import time,re 
from functools import lru_cache

def loadfile(file):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    return [list(line) for line in lines]

def countpaths(grid):
    start = grid[0].index('S')
    H = len(grid)
    W = len(grid[0])

    @lru_cache(None)
    def go(row, col):
        row += 1
        if row >= H or col < 0 or col >= W:
            return 0
        if row == H - 1:
            return 1
        if grid[row][col] == '.':
            return go(row, col)
        return go(row, col - 1) + go(row, col + 1)
    return go(0, start)

def solve(p):
    p1 = p2 = 0
    tachyon_manifold = p
    beams =  [tachyon_manifold[0].index('S')]
    for line in tachyon_manifold[1:]:
        new_beams = []
        for beam in beams:
            if beam < 0 or beam >= len(line):
                continue
            if line[beam] == '.' : 
                new_beams.append(beam)
                continue
            else:
                new_beams.append(beam-1)
                new_beams.append(beam+1)
            p1 += 1
        beams = list(set(new_beams))
    p2 = countpaths(tachyon_manifold)
    return p1,p2

        
    print(start)
    print(tachyon_manifold)

time_start = time.perf_counter()
print(f"Solution: {solve(loadfile('day7.txt'))}")
print(f"Thought for {time.perf_counter() - time_start:.6f} Seconds")