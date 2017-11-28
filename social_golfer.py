# https://www.codewars.com/kata/556c04c72ee1147ff20000c9/train/python
from itertools import permutations
import scipy.special

a = [['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
     ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
     ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
     ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
     ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']]

players = set("".join(a[0]))
groups = sum(a, [])
# every player plays once every day
h = [set("".join(i)) for i in a] * 2
if h != h[::-1]:
    print("DAY", False)

# the grop sizes are the same every day
if len(set(len(i) for i in groups)) != 1:
    print("GS", False)

# same amount of groups every day
if len(set(len(i) for i in a)) != 1:
    print("GD", False)

players = set("".join(a[0]))
l =  len(set.union(*[set(permutations(g, 2)) for g in groups]))
if l != scipy.special.binom(len(groups[0], 2):
    print("BINOM", False)