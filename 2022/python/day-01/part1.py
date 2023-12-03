with open("input") as data:
    print(
        max(
            sum(int(cal) for cal in elf.split("\n"))
            for elf in data.read().split("\n\n")
        )
    )
