class Monkey:
    def __init__(self, items, operation_str, divis_test, monkey_true, monkey_false):
        self.items = items
        self.operation_str = operation_str
        self.divis_test = divis_test
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false

    def resultant_monkey(self, worry_level):
        return (
            self.monkey_true
            if worry_level % self.divis_test == 0
            else self.monkey_false
        )

    def exec_operation(self, old):
        return eval(self.operation_str)


class Game:
    def __init__(self):
        self.monkeys = []
        self.init_monkeys()
        self.monkeys_inspection_count = [0] * len(self.monkeys)

    def init_monkeys(self):
        with open("input") as data:
            for monkey_data in data.read().split("\n\n"):
                lines = [line.strip() for line in monkey_data.split("\n")]
                self.monkeys.append(
                    Monkey(
                        items=[int(n) for n in lines[1][16:].split(", ")],
                        operation_str="".join(lines[2].split()[-3:]),
                        divis_test=int(lines[3].split()[-1]),
                        monkey_true=int(lines[4].split()[-1]),
                        monkey_false=int(lines[5].split()[-1]),
                    )
                )

    def play_round(self):
        for curr_monkey_num, monkey in enumerate(self.monkeys):
            while len(monkey.items) > 0:
                worry_level = monkey.exec_operation(monkey.items.pop(0)) // 3
                new_monkey_num = monkey.resultant_monkey(worry_level)
                self.monkeys[new_monkey_num].items.append(worry_level)
                self.monkeys_inspection_count[curr_monkey_num] += 1


game = Game()
for i in range(20):
    game.play_round()
top_two = sorted(game.monkeys_inspection_count, reverse=True)[:2]
print(top_two[0] * top_two[1])
