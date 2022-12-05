# I have to admit parsing these values is a bit annoying

data = [i.strip('\n') for i in open('./input_day05.txt')]

# separation between stack and moves
cut = data.index('')

stacks = data[:cut]

nstacks = len(stacks[-1].replace(' ', ''))

nrows = len(stacks) - 1

# encode stacks

lists = [[] for _ in range(nstacks)]

for row in stacks[:-1]:
    values = []
    idx = 1

    list_idx = 0

    while len(values) < nstacks:
        values.append(row[idx])

        if row[idx] != ' ':
            lists[list_idx].append(row[idx])
        idx += 4
        list_idx += 1


for i, instruction in enumerate(data[cut+1:]):
    idx = int(instruction.split('move ')[1].split(' ')[0])
    origin = int(instruction.split('from ')[1].split(' ')[0])
    destination = int(instruction.split('to ')[1])

    to_be_moved = lists[origin-1][:idx]
    lists[origin-1] = lists[origin-1][idx:]
    lists[destination-1] = to_be_moved[::-1] + lists[destination-1]

print("Part 1:", ''.join(i[0] for i in lists))


# Part 2 is almost the same, just no reverse ordering when moving stacks


lists = [[] for _ in range(nstacks)]

for row in stacks[:-1]:
    values = []
    idx = 1

    list_idx = 0

    while len(values) < nstacks:
        values.append(row[idx])

        if row[idx] != ' ':
            lists[list_idx].append(row[idx])
        idx += 4
        list_idx += 1


for i, instruction in enumerate(data[cut+1:]):
    idx = int(instruction.split('move ')[1].split(' ')[0])
    origin = int(instruction.split('from ')[1].split(' ')[0])
    destination = int(instruction.split('to ')[1])

    to_be_moved = lists[origin-1][:idx]
    lists[origin-1] = lists[origin-1][idx:]
    lists[destination-1] = to_be_moved[::1] + lists[destination-1]

print("Part 2:", ''.join(i[0] for i in lists))
