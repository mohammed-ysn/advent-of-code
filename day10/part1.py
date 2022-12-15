class CPU:
    def __init__(self):
        self.cycle = 1
        self.X = 1
        self.signal_strengths_sum = 0

    def incr_cycle(self):
        if self.cycle in range(20, 221, 40):
            self.signal_strengths_sum += self.cycle * self.X
        self.cycle += 1


cpu = CPU()
with open("input") as data:
    for line in data:
        split_line = line.rstrip().split()

        instr = split_line[0]
        if instr == "noop":
            cpu.incr_cycle()
            continue

        incrX = int(split_line[1])
        cpu.incr_cycle()
        cpu.incr_cycle()
        cpu.X += incrX

print(cpu.signal_strengths_sum)
