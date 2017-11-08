import numpy as np


def solution1(strng):
    strlist = strng.split()
    digitsum = np.fromiter(
        map(lambda x: sum(map(int, x)), strlist), dtype=np.int)
    values = np.fromiter(map(int, strlist), dtype=np.int)
    sortedkey = digitsum + values / (max(values) + 1)
    resultlist = [x for _, x in sorted(zip(sortedkey, strlist))]
    return " ".join(resultlist)


def solution2(_str):
	return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))


_str = "58 10 11 92 29 31"
s1 = sorted(_str.split(" ")) 
s2 = sorted(s1, key=lambda x: sum(int(c) for c in x))