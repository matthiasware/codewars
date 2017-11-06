import timeit
import itertools
from timeit import Timer
# t max sum of distances
# k number of towns
# ls list of sitances
# (k ls)


# t max sum of distances
# k number of towns
# ls list of sitances
# (k ls)
def choose_best_sum(t, k, ls):
    pool = tuple(sorted(ls))
    n = len(pool)
    if k > n or k < 1 or t < 1:
        return None
    indices = list(range(k))
    best = (indices, sum([pool[i] for i in indices]))
    while True:
        for i in reversed(range(k)):
            if indices[i] != n + i - k:
                break
        else:
            break
        indices[i] += 1
        for j in range(i + 1, k):
            indices[j] = indices[j - 1] + 1
        s = sum([pool[i] for i in indices])
        if s > t:
            indices[i] = n + i - k
        elif s == t:
            best = (indices, s)
            break
        elif s > best[1]:
            best = (indices, s)
    if best[1] > t:
        return None
    return best[1]


def choose_best_sum2(t, k, ls):
    try:
        return max(sum(i) for i in itertools.combinations(ls, k) if sum(i) <= t)
    except Exception:
        return None


def w(t, k, ls):
    def wrapper():
        return choose_best_sum(t, k, ls)
    return wrapper

def w2(t, k, ls):
    def wrapper():
        return choose_best_sum2(t, k, ls)
    return wrapper


if __name__ == "__main__":
    ls = [66, 75, 11, 12, 98, 14, 22, 50, 55, 57, 58, 60, 22, 74, 33, 29, 63]
    t = 400
    k = 6
    time2 = timeit.timeit(w(t, k, ls), number=1000)
    time = timeit.timeit(w2(t, k, ls), number=1000)
    print("Sorted: ", time)
    print("Unsorted: ", time2)
