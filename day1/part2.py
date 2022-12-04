with open("input") as data:
    elves = sorted(
        (sum(int(cal) for cal in elf.split("\n")) for elf in data.read().split("\n\n")),
        reverse=True,
    )[:3]

    print(sum(elves))
