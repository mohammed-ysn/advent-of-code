from collections import defaultdict


def first_unique_seq_pos(chars, n):
    counts = defaultdict(int)
    # add first n chars to dict without checking
    for char in chars[:n]:
        counts[char] += 1
    processed_chars = n
    if len(counts) == n:
        return processed_chars

    for i in range(n, len(chars)):
        char_to_remove = chars[i - n]
        counts[char_to_remove] -= 1
        if counts[char_to_remove] == 0:
            del counts[char_to_remove]
        counts[chars[i]] += 1
        processed_chars += 1
        if len(counts) == n:
            return processed_chars


with open("input") as data:
    p = first_unique_seq_pos(data.read(), 14)
    print(p)
