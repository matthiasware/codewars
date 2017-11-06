from collections import defaultdict
import numpy as np


strng = "2000 10003 1234000 44444444 9999 11 11 22 123"
lst = strng.split()
qsum = np.array(list(map(lambda x: sum(map(int, list(x))), lst)))
weight = np.array(list(map(int, lst)))
factors = max(qsum)/qsum
qsum = factors * qsum
weight = factors * weight
final = weight/qsum

o = [x for _, x in sorted(zip(final, lst))]

# k = [(x, q) for x, q in sorted(zip(qsum, lst))]
# dfd = defaultdict(list)
# for k,v in k:
# 	dfd[k].append(int(v))
# j = list(map(sorted, dfd.values()))

# o = zip(dfd.keys(), j)


