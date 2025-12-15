import time, re
def loadfile(file):
    c = []
    with open(file) as f:
       for lines in f.readlines():
        c.append(lines.strip())
    return c
        
def solve(p):
    x = 0
    for banks in p:
        joltages = [int(j) for j in banks]
        l = len(str(banks))
        i = joltages.index(max(joltages)) 
        if i < l-1:
            newj = joltages[i+1:] 
            j = newj.index(max(newj))
            print(f'{joltages[i]} + {joltages[i+j+1]}')
            x += int(str(joltages[i]) + str(joltages[i+j+1]))
        else:
            newj = joltages.copy()
            newj.pop(i)
            j = newj.index(max(newj))
            print(f'{joltages[j]} + {joltages[i]}')
            x += int(str(joltages[j]) + str(joltages[i]))
    return x



        
    





time_start = time.perf_counter()
print(f'Solution {solve(loadfile('day3.txt'))}')
print(f'Thought for {time.perf_counter() - time_start:.6f} Seconds')
 