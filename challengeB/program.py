#!/usr/bin/env python3

from collections import defaultdict
import sys

def find_isomorph(words: list[str]) -> bool:
    mapping = defaultdict(str)
    cond = True
    i = 0
    while i < len(words[0]):
        char1 = words[0][i]
        char2 = words[1][i]

        i += 1
        if char1 in mapping:
            if char2 == mapping[char1]:
                continue
            else:
                cond = False
        else:
            mapping[char1] = char2

    return cond

def main():
    while True:
        line  = sys.stdin.readline().strip()

        if not line:
            break

        words = line.split()
        if find_isomorph(words):
            print("Isomorphic")
        else:
            print("Not Isomorphic")



    return

if __name__ == "__main__":
    main()