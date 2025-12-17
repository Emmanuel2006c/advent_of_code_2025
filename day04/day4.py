import time,re

def loadfile(file):
    with open(file) as f:
        paperstorage = []
        levels = f.readlines()
        for level in levels:
             paperstorage.append([position for position in level])
        return{(x,y) for y, row in enumerate(paperstorage)
                     for x, position in enumerate(row) if position == '@'}

def neighbourpositions(x,y,p):
    neighbours = {(x+1,y),(x-1,y),(x,y-1),(x,y+1),(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1)}
    return p & neighbours
    
 
def solve(p):
    p1 = p2 = 0
    for x,y in p:
        p1 += len(neighbourpositions(x,y,p)) < 4
    
    while True:
        changes = False
        removablepaperrolls = set()
        for x,y in p:
            if len(neighbourpositions(x,y,p)) < 4:
                removablepaperrolls.add((x,y))
                p2+= 1
                changes = True
        p -= removablepaperrolls
        if changes == False: break   
    return p1,p2


        

time_start = time.perf_counter()
print(f"Solution: {solve(loadfile("day4.txt"))}")
print(f"Thought for {time.perf_counter() - time_start:.6f} Seconds")


'''
    for neighbourx, neighboury in {(x+1,y),(x-1,y),(x,y-1),(x,y+1),(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1)}:
        if (neighbourx,neighboury) not in p: continue
        neighbours += 1
    return neighbours

'''
'''
def sweepthrough(x,y,p):
    removedpaperrolls = 0
    for x,y in p:
         removedpaperrolls += neighbourpositions(x,y,p) < 4
         p.remove((x,y))
    return removedpaperrolls

def solve(p):
    p1 = 0
    p1 += sweepthrough(x,y,p)
    
    return p1
'''
