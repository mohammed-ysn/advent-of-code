class System:
    def __init__(self):
        self.cycle = 1
        self.X = 1
        self.display = [["."] * 40 for _ in range(6)]

    def incr_cycle(self):
        draw_y, draw_x = divmod((self.cycle - 1), 40)
        if (self.X - 1) <= draw_x <= (self.X + 1):
            self.display[draw_y][draw_x] = "#"
        self.cycle += 1

    def print_display(self):
        for row in self.display:
            print(row)


system = System()
with open("input") as data:
    for line in data:
        split_line = line.rstrip().split()

        instr = split_line[0]
        if instr == "noop":
            system.incr_cycle()
            continue

        incrX = int(split_line[1])
        system.incr_cycle()
        system.incr_cycle()
        system.X += incrX

system.print_display()
