def heapsort(lst):
    pass


def mergesort(lst):
    pass


def quicksort(lst):
    pass


def insertionsort(lst):
    for j in range(1, len(lst)):
        i = j - 1
        k = lst[j]
        while i >= 0 and lst[i] > k:
            lst[i + 1] = lst[i]
            i = i - 1
        lst[i + 1] = k


def bubblesort(lst):
    issorted = False
    while not issorted:
        issorted = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                issorted = False


def selectionsort(lst):
    for j in range(len(lst)):
        minimum = j
        for i in range(j + 1, len(lst)):
            if lst[minimum] > lst[i]:
                minimum = i
        lst[j], lst[minimum] = lst[minimum], lst[j]


def timsort(lst):
    pass


lst = [6, 2, 3, 1, 4, 0, 5]

# insertionsort(lst)
# selectionsort(lst)
bubblesort(lst)
print(lst)