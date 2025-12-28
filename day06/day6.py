import time,re,math

def loadfile(file):
    with open(file) as f:
        lines = f.readlines()
        numbers = [re.findall(r'\d+', line) for line in lines[:-1]]
        operators = list(lines[-1].replace(' ',''))
    return numbers,operators

def solve(p):
    p1 = p2 = 0
    numbers, operators = p
    numberstransposed = list(map(list,zip(*numbers)))
    for i,row in enumerate(numberstransposed):
        print(row,operators[i])
        if operators[i] == '*':
            p1 += math.prod(map(int,row))
        if operators[i] == '+':
            p1 += sum(map(int,row))
    for i,row in enumerate(numberstransposed): 
        digits = list(list(d for d in n) for n in row)
        reversedigits = [listofdigits[::-1] for listofdigits in digits]
        hexalophodnumbers = []
        max_len = max(map(len,reversedigits))
        for k in range(max_len):
            s = ''
            for lst in reversedigits:
                if k < len(lst):
                    s = s+lst[k] 
            hexalophodnumbers.append(s)
        print(hexalophodnumbers) 
    return p1


time_start = time.perf_counter()
print(f"Solution: {solve(loadfile('day6.txt'))}")
print(f"Thought for {time.perf_counter() - time_start:.6f} Seconds")