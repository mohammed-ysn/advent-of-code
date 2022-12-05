overlap_count = 0
with open("input") as data:
    for line in data:
        vals = [rnge.split("-") for rnge in line.rstrip().split(",")]
        (l1, r1), (l2, r2) = tuple((int(n), int(m)) for n, m in vals)
        if (
            # second range starts in first
            (l1 <= l2 <= r1)
            # second range ends in first
            or (l1 <= r2 <= r1)
            # first range starts in second
            or (l2 <= l1 <= r2)
            # first range ends in second
            or (l2 <= r1 <= r2)
        ):
            overlap_count += 1
print(overlap_count)
