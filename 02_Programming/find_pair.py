import sys

DEBUG = 1
TESTCASE = 'input_file.txt'


def findpair(d, some_value):
    for k in d.keys():
        if some_value-k in d:
            print(d[some_value-k], some_value-k, ',', d[k], k)
            return


def parse():

    if DEBUG:
        with open(TESTCASE) as f:
            lines = f.readlines()
    else:
            lines = sys.stdin.readlines()

    d = {}
    for line in lines:
        k, v = line.strip('\n').split(' ')
        d[int(v)] = k
    return d


if __name__=='__main__':
    d = parse()
    findpair(d, 25)