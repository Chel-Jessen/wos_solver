import string
from itertools import permutations


def solve():
    chars = [char for char in input("Enter letters: ").strip()]
    min_len = 4
    max_len = len(chars)

    words = {''.join(perm).upper() for length in range(min_len, max_len + 1) for perm in permutations(chars, length)}
    dictionary = set(open('words.txt', "r", encoding="utf-8").read().strip().split())
    return sorted(list(words & dictionary), key=len, reverse=False)

def build_wordlist():
    with open('words.txt', "w", encoding="utf-8") as f:
        for line in open("dictionary.txt", "r", encoding="utf-8").readlines():
            if line == "\n":
                continue
            line = line.split(" ")[0]
            if len(line) < 4:
                continue
            if any(filter(lambda char: char not in string.ascii_letters, line)):
                continue
            f.write(line.strip().upper() + "\n")


if __name__ == '__main__':
    [print(word) for word in solve()]
