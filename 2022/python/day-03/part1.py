def get_priority(item_letter):
    if item_letter.islower():
        return ord(item_letter) - 96

    return ord(item_letter) - 38


def main():
    repeated_items_priorities_sum = 0
    with open("input") as data:
        for rucksack in data:
            rucksack = rucksack.rstrip()
            halfway_point = len(rucksack) // 2
            left_items, right_items = rucksack[:halfway_point], set(
                rucksack[halfway_point:]
            )
            for item in left_items:
                if item in right_items:
                    repeated_items_priorities_sum += get_priority(item)
                    break
    print(repeated_items_priorities_sum)


main()
