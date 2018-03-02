import numpy as np

filename = 'a_example.in'


def distance(ride):
    return abs(ride[0]-ride[2]) + abs(ride[1]-ride[3])


def load_file(fname):
    with open(fname, "r") as fo:
        r, c, f, n, b, t = list(map(lambda x: int(x), fo.readline().split()))
        data = list(map(lambda x: list(map(lambda y: int(y),  x.split() )),
                        fo.read().split('\n')))

    tm = np.array(data)
    return [r, c, f, n, b, t, tm]


def print_file(fname, data):
    global f
    with open(fname, "r") as fo:
        for i in range(f):
            fo.write()

r, c, f, n, b, t, tm = load_file(filename)
print([r, c, f, n, b, t, tm])