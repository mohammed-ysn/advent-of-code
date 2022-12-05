with open("input") as data:
    stack_data, move_data = (data_i.split("\n") for data_i in data.read().split("\n\n"))

# remove numbering row
stack_data.pop()

# manipulate move data into following format
# list of (move_count, source_stack, target_stack)
# note: 0-indexed stack numbers
for i in range(len(move_data)):
    move = move_data[i].split()
    move_data[i] = (int(move[1]), int(move[3]) - 1, int(move[5]) - 1)

# construct stacks
stacks = []
for i in range(1, len(stack_data[0]), 4):
    stacks.append(
        [stack_data[j][i] for j in range(len(stack_data)) if stack_data[j][i] != " "]
    )

# perform moves
for n, source, target in move_data:
    for i in range(n):
        stacks[target].insert(0, stacks[source].pop(0))

# print top crate of each stack
top_items = [s[0] for s in stacks]
print("".join(top_items))
