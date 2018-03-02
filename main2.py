import numpy as np
import random

filename = 'd_metropolis'
initial_score = 2258322


def distance(ride):
    return abs(ride[0]-ride[2]) + abs(ride[1]-ride[3])


def load_file(fname):
    with open(fname+'.in', "r") as fo:
        r, c, f, n, b, t = list(map(lambda x: int(x), fo.readline().split()))
        data = list(map(lambda x: list(map(lambda y: int(y),  x.split() )),
                        fo.read().split('\n')))

    tm = np.array(data)
    return [r, c, f, n, b, t, tm]


def score(result):
    global f, tm, b
    total_score = 0
    current_step = 0
    for i in range(f):
        for j in range(1,len(result[i])):
            ride = tm[j]
            dist = distance(ride)
            if(current_step <= ride[4]):
                current_step = ride[4]
                total_score += b
            if(dist+current_step < ride[5]):
                total_score += dist
    return total_score


def print_file(fname, data):
    global f
    with open(fname+'.out', "w+") as fo:
        for i in range(f):
            line = str(len(data[i])) + " "+" ".join(list(map(lambda x: str(x), data[i])))+"\n"
            fo.write(line)

r, c, f, n, b, t, tm = load_file(filename)
result = []
for i in range(f):
    result.append([])

current_score=0
#while(current_score<=initial_score):
for i in range(n):
    fleet = random.randint(0, f-1)
    result[fleet].append(i)
current_score = score(result)
print(current_score)
print_file(filename, result)
