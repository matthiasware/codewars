def capitalize(s):
    e = list(s)
    o = list(s)
    e[0::2] = map(str.upper, e[0::2])
    o[1::2] = map(str.upper, o[1::2])
    return ["".join(e), "".join(o)]


def capitalize(s):
    e = [item.upper() if idx % 2 == 0 else item for idx, item in enumerate(s)]
    o = [item.upper() if idx % 2 == 1 else item for idx, item in enumerate(s)]
    return ["".join(e), "".join(o)]

print(capitalize("abcdefg"))

