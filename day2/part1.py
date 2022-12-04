standard_move = {
    "X": "r",
    "Y": "p",
    "Z": "s",
    "A": "r",
    "B": "p",
    "C": "s",
}

move_score = {
    "r": 1,
    "p": 2,
    "s": 3,
}

winning_moves = {
    "r": "s",
    "p": "r",
    "s": "p",
}

with open("input") as data:
    score = 0
    for line in data:
        opponent, me = (standard_move[move] for move in line.rstrip().split(" "))
        score += move_score[me] + (
            6 if opponent == winning_moves[me] else (3 if opponent == me else 0)
        )
    print(score)
