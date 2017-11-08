import numpy as np


strng = "10 11 29 92 58"
lst = strng.split()
qsum = np.array(list(map(lambda x: sum(map(int, list(x))), lst)))
weight = np.array(list(map(int, lst)))
factors = (qsum / max(qsum)) ** (len(qsum) ** len(qsum))
final = weight * factors
o = [x for _, x in sorted(zip(final, lst))]
" ".join(o)