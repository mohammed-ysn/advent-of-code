standard_move = {
    "A": "r",
    "B": "p",
    "C": "s",
}

move_score = {
    "r": 1,
    "p": 2,
    "s": 3,
}


def get_required_move(opponent, outcome):
    if outcome == "Y":
        return opponent

    return {
        "r": {"X": "s", "Z": "p"},
        "p": {"X": "r", "Z": "s"},
        "s": {"X": "p", "Z": "r"},
    }[opponent][outcome]


def main():
    with open("input") as data:
        score = 0
        for line in data:
            opponent, outcome = line.rstrip().split(" ")
            opponent = standard_move[opponent]

            score += move_score[get_required_move(opponent, outcome)] + (
                6 if outcome == "Z" else (3 if outcome == "Y" else 0)
            )
        print(score)


main()
