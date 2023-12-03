import numpy as np

rope_length = 10
rope = np.zeros(shape=(rope_length, 2), dtype=int)
visited = {tuple(rope[-1])}

direction_map = {
    "U": np.array([0, 1]),
    "D": np.array([0, -1]),
    "R": np.array([1, 0]),
    "L": np.array([-1, 0]),
}

with open("input") as data:
    for line in data:
        split_line = line.rstrip().split()

        head_direction = direction_map[split_line[0]]
        count = int(split_line[1])

        for _ in range(count):
            # move head
            rope[0] += head_direction

            # move all other knots in rope
            for i in range(1, rope_length):
                distance = rope[i] - rope[i - 1]
                if np.any(abs(distance) == 2):
                    rope[i] = rope[i - 1] + (distance / 2).astype(int)

            visited.add(tuple(rope[-1]))

print(len(visited))
