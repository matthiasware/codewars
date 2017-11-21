# https://www.codewars.com/kata/55f9ee4d8f3bbabf2200000c/train/python


def norm2(vec):
    return sum(i**2 for i in vec)**0.5


lizt = [(-5, 3, -5), (3, 5, -6), (-5, 6, 0),
        (-5, 3, -6), (4, -3, -1), (5, 4, -3),
        (6, 4, -1), (5, 3, 2), (1, -2, 5),
        (-5, 0, -2)]

l = max(abs(n) for sl in lizt for n in sl)
N_c = len(lizt)
N_s = len([v for v in lizt if norm2(v) <= l])
pi_est = round(N_s / float(N_c) * 6, 4)
pi = 3.141592653589793
err = round(abs(pi - pi_est) / pi * 100, 2)
