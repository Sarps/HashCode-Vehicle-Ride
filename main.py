import numpy as np

filenames = ('a_example', 'b_should_be_easy', 'c_no_hurry', 'd_metropolis', 'e_high_bonus')


def distance(ride):
    return abs(ride[0]-ride[2]) + abs(ride[1]-ride[3])


def load_file(fname):
    dtype = [('a', int), ('b', int), ('x', int), ('y', int), ('s', int), ('f', int), ('i', int)]
    with open(fname+'.in', "r") as fo:
        r, c, f, n, b, t = list(map(lambda x: int(x), fo.readline().split()))
        lines = fo.read().rstrip('\n').split('\n')
        data = list(map(lambda x: tuple(map(int,  x[1].split()+[x[0]])),
                        enumerate(lines)))

    tm = np.array(data, dtype=dtype)
    return [r, c, f, n, b, t, tm]


def print_file(fname, data):
    global f
    with open(fname+'.out', "w+") as fo:
        for i in range(f):
            line = str(len(data[i])) + " "+" ".join(list(map(lambda x: str(x), data[i])))+"\n"
            fo.write(line)


def score(result):
    print(result)
    global f, tm, b
    total_score = 0
    for i in range(f):
        current_step = 0
        for j in result[i]:
            ride = tm[j]
            dist = distance(ride)
            if(current_step <= ride['s']):
                total_score += b
                current_step = ride['s']
            if(dist+current_step < ride['f']):
                total_score += dist
            current_step += dist
    return total_score


def gen_array():
    global f
    result = []
    for i in range(f):
        result.append([])
    return result


def algorithm(stm):
    global f
    assigned = []
    current_step, i_ride, i_fleet, result = 0, 0, 0, gen_array()
    while len(assigned) < len(stm) and i_fleet < f:
        if i_ride >= len(stm):
            i_fleet += 1
            current_step = i_ride = 0
            continue
        ride = stm[i_ride]
        if current_step > ride['s'] or i_ride in assigned:
            i_ride += 1
            continue
        result[i_fleet].append(ride['i'])
        assigned.append(i_ride)
        current_step = ride['s'] + distance(ride)
    return result


def run(filename):
    global r, c, f, n, b, t, tm, stm
    r, c, f, n, b, t, tm = load_file(filename)
    stm = np.sort(tm, order=['s', 'f'])
    result = algorithm(stm)
    print(score(result))
    print_file(filename, result)


if __name__ == '__main__':
    for filename in filenames:
        run(filename)

