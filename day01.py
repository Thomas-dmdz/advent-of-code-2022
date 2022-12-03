from collections import defaultdict

data = [i.strip('\n') for i in open('./input_day01.txt')]

id = 0
d = defaultdict(int)

for val in data:
    if val == '':
        id += 1
    else:
        d[id] += int(val)

print("Part 1:", max([val for val in d.values()]))

import random

# O(n) time
def qselect(i:int, a:list)->int:
    if a == []:
        return []
    idx = random.randint(0, len(a) - 1)
    pivot = a[idx]

    a[0], a[idx] = a[idx], a[0]

    left = [x for x in a if x < pivot]
    len_left = len(left)
    if len_left == i - 1:
        return pivot
    elif len_left < i - 1:
        right = [x for x in a[1:] if x >= pivot]
        return qselect(i - len_left - 1, right)
    else:
        return qselect(i,left)

# negative so kth smallest gives kth largest
li = [-val for val in d.values()]


kth = qselect(3, li)
print("Part 2:", -sum([i for i in li if i <= kth]))
