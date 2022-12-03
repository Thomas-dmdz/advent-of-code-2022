# encode game rules

# reward for shape
shape_score = dict(zip(list('XYZ'), range(1, 4)))

# reward for outcome
outcome_score = {'A': {'X': 3, 'Y': 6, 'Z': 0}, 'B': {'X': 0, 'Y': 3, 'Z': 6}, 'C': {'X': 6, 'Y': 0, 'Z': 3}}

# read input i.e. rock paper scissors games
data = [i.strip('\n').split(' ') for i in open('./input_day02.txt')]

print("Part 1:", sum(outcome_score[p1][p2] + shape_score[p2] for (p1, p2) in data))

expected_move = {'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'}, 'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'}, 'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'}}
desired_outcome = dict(zip(list('XYZ'), [0, 3, 6]))


print("Part 2:", sum(desired_outcome[p2] + shape_score[expected_move[p1][p2]] for (p1, p2) in data))
