contained_count = 0
with open("input") as data:
    for line in data:
        vals = [rnge.split("-") for rnge in line.rstrip().split(",")]
        (l1, r1), (l2, r2) = tuple((int(n), int(m)) for n, m in vals)
        if (l1 <= l2 and r1 >= r2) or (l2 <= l1 and r2 >= r1):
            contained_count += 1
print(contained_count)
