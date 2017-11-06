class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        if self.next:
            return str(self.data) + "->" + self.next.__str__()
        else:
            return "None"

    __repr__ = __str__


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.first_head = first
        self.second_head = second


def als(head):
    if head is None or head.next is None:
        raise Exception
    context = Context(Node(), Node())
    l = 0
    while head is not None:
        node = Node(head.data)
        if l % 2 == 0:
            context.first.next = node
            context.first = node
        else:
            context.second.next = node
            context.second = node
        l += 1
        head = head.next
    context.first = context.first_head.next
    context.second = context.second_head.next
    return context


def makeNodes(i):
    if type(i) == int:
        n = Node()
        first = n
        for j in range(i):
            k = Node(j)
            n.next = k
            n = k
        return first.next
    else:
        i = [Node(k) for k in i]
        for j in range(len(i) - 1):
            i[j].next = i[j + 1]
    return i[0]

nl = makeNodes([5, 6, 1, 2, 3, 3, 3, 4, 8, 5, 4, 1])

