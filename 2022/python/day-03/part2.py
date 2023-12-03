def get_priority(item_letter):
    if item_letter.islower():
        return ord(item_letter) - 96

    return ord(item_letter) - 38


def main():
    badge_priorities_sum = 0
    with open("input") as data:
        while True:
            # get next three lines
            lines_character_sets = [set(data.readline().rstrip()) for _ in range(3)]

            if len(lines_character_sets[0]) == 0:
                # end of file reached
                break

            # find item in each of the lines
            s = lines_character_sets[0]
            s.intersection_update(lines_character_sets[1])
            s.intersection_update(lines_character_sets[2])

            badge_priorities_sum += get_priority(s.pop())

    print(badge_priorities_sum)


main()
