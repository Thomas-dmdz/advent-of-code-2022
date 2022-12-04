data = [i.strip('\n') for i in open('./input_day04.txt')]

# separate section bounds
data = [x.replace(',', '-').split('-') for x in data]

# convert to integer
data = [[int(bound) for bound in span] for span in data]

print("Part 1:", sum((a >= c) & (b <= d) or (a <= c) & (b >= d) for a, b, c, d in data))

# Part 2

# n - count no overlap
print("Part 2:", len(data) - sum(b < c or a > d for a, b, c, d in data))
