def permutate(given, s, prefix, n, k):
    if k == 0:
        printString(prefix, given)
        return

    for i in range(n):
        permutate(given, s, prefix + s[i], n, k - 1)


def printString(prefix, given):
    p = list(prefix)
    g = list(given)
    for x, j in enumerate(g):
        if j == 'X':
            g[x] = p.pop()
    print(''.join(g))


if __name__=='__main__':
    s = '01'
    given1 = '10X10X0'
    c1 = given1.count('X')
    given2 = 'X0'
    c2 = given2.count('X')
    permutate(given1, s, '', len(s), c1)
    permutate(given2, s, '', len(s), c2)

'''
Time Complexity is O(2^X) , where X is the number of empty slots to fill in the string.
'''
