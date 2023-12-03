with open("input") as data:
    grid = [list(map(int, line.rstrip())) for line in data]

num_rows = len(grid)
num_cols = len(grid[0])
visible_count = 0
for i in range(num_rows):
    for j in range(num_cols):
        tree_height = grid[i][j]
        if (
            all(tree_height > grid[i][k] for k in range(j))
            or all(tree_height > grid[i][k] for k in range(j + 1, num_cols))
            or all(tree_height > grid[k][j] for k in range(i))
            or all(tree_height > grid[k][j] for k in range(i + 1, num_rows))
        ):
            visible_count += 1
print(visible_count)
