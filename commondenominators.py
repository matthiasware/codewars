# kgv(m, n) = |m*n|/ggt(m,n)
# kgv(a, b, c) = kgv(a, (kgv(b, c)))
# ggt(m,n) ... euclidean algorithm
from functools import reduce


def ggt(a, b):
    while b:
        a, b = b, a % b
    return a


def kgv(a, b):
    return a * b // ggt(a, b)


def l(x):
    return reduce(kgv, x)


def convertFracts(lst):
    cf = reduce(kgv, [x[1] for x in lst])
    return [[cf * x[0], kgv * x[1]] for x in lst]

a = [3, 6, 9]