import numpy as np


num_signs = 1000
x = np.array(range(num_signs))
px = np.ones(len(x)) / len(x)
ix = -1 * np.log2(px)
e_ud = sum(px * ix)

px = [1 / 2**(i + 1) for i in range(len(x) - 1)] + [1 / 2**(len(x) - 1)]
ix = -1 * np.log2(px)
e_nu = sum(px * ix)
e_max = np.log2(num_signs)

print("H_max:", e_max)
print("H_uni:", e_ud)
print("H_nuni:", e_nu)
print("Redundancy for uni:", e_max - e_ud)
print("Redundancy for non-uni:", e_max - e_nu)
print("H_uni/H_max:", e_ud / e_max)
print("H_nuni/H_max:", e_nu / e_max)
