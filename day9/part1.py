import numpy as np


def head_touching_tail(head, tail):
    col_and_row_dist = head - tail
    return abs(col_and_row_dist[0]) <= 1 and abs(col_and_row_dist[1]) <= 1


def main():
    head = np.array([0, 0])
    tail = np.array([0, 0])
    seen = {(0, 0)}

    direction_map = {
        "U": np.array([0, 1]),
        "D": np.array([0, -1]),
        "R": np.array([1, 0]),
        "L": np.array([-1, 0]),
    }

    with open("input") as data:
        for line in data:
            split_line = line.rstrip().split()
            direction = direction_map[split_line[0]]
            count = int(split_line[1])
            for _ in range(count):
                # move head
                head += direction

                if head_touching_tail(head, tail):
                    continue

                # move tail
                if head[0] == tail[0] or head[1] == tail[1]:
                    tail += direction
                else:
                    tail = head - direction

                seen.add(tuple(tail))

    print(len(seen))


main()
