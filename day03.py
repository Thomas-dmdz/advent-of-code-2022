import string

data = [i.strip('\n') for i in open('./input_day03.txt')]

# intersection of set to get common letter
letters = [list(set(x[:len(x)//2]) & set(x[len(x)//2:]))[0] for x in data]

priority = dict(zip(string.ascii_letters, range(1, len(string.ascii_letters) + 1)))

print("Part 1:", sum(priority[letter] for letter in letters))

# maybe a more efficient apprach:
s = 0
for x in data:
    idx = 0
    while x[idx] not in set(x[len(x)//2:]):
        idx += 1
    s += priority[x[idx]]
print("Part 1 method 2:", s)


# Part 2

print("Part 2:", sum(priority[list(set(x) & set(y) & set(z))[0]] for x, y, z in zip(data[0::3], data[1::3], data[2::3])))
