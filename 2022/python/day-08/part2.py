with open("input") as data:
    grid = [list(map(int, line.rstrip())) for line in data]

num_rows = len(grid)
num_cols = len(grid[0])
max_vis = 0
for i in range(num_rows):
    for j in range(num_cols):
        tree_height = grid[i][j]
        l, r, u, d = 0, 0, 0, 0
        for k in range(j - 1, -1, -1):
            l += 1
            if grid[i][k] >= tree_height:
                break
        for k in range(j + 1, num_cols):
            r += 1
            if grid[i][k] >= tree_height:
                break
        for k in range(i - 1, -1, -1):
            u += 1
            if grid[k][j] >= tree_height:
                break
        for k in range(i + 1, num_rows):
            d += 1
            if grid[k][j] >= tree_height:
                break
        max_vis = max(max_vis, (l * r * u * d))

print(max_vis)
