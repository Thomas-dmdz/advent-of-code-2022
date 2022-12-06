data = [i.strip('\n') for i in open('./input_day06.txt')][0]

# naive approach
def n_char_before_start_msg(stream_length):
    idx = 0
    while len(set(data[idx:idx+stream_length])) < stream_length:
        idx += 1
    return idx + stream_length

print("Part 1:", n_char_before_start_msg(4))
print("Part 2:", n_char_before_start_msg(14))
