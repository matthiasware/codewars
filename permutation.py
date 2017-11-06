def per(s):
    s = sorted(list(s))
    if len(s)%2 == 0:
        r = [s.pop(len(s) // 2 - 1)] + s[::-1]
    else:
        f = s.pop(len(s) // 2)
        n = [s.pop(len(s) // 2 - 1)] + s[::-1]
        r = [f] + n
    return "".join(r)

per("abc")