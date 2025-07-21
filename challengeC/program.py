#!/usr/bin/env python3

import sys
from itertools import product

# global vars

OPERATORS = ['+', '-', '*']
NUMBERS   = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# construct the expression
def build_expr(operators: list[str]) -> str:
    expression = (
        #(((9 ? 8)
        f"((({NUMBERS[0]} {operators[0]} {NUMBERS[1]})"
        # ? 7) ? 6)
        f" {operators[1]} {NUMBERS[2]}) {operators[2]} {NUMBERS[3]})"
        # ? (5 ? (4
        f" {operators[3]} ({NUMBERS[4]} {operators[4]} ({NUMBERS[5]}"
        # ? (3 ? (2 ? 1))))
        f" {operators[5]} ({NUMBERS[6]} {operators[6]} ({NUMBERS[7]} {operators[7]} {NUMBERS[8]}))))"
    )

    return expression

def main():
    while True:
        target = sys.stdin.readline().strip()
        if not target:
            break

        target = int(target)

        # cartesian product of all combos of operators to try
        for combo in product(OPERATORS, repeat=8):
            # build the string to be evaluated
            expr = build_expr(list(combo))

            # evaluate the string and check if equal to target
            if eval(expr) == target:
                print(expr + f" = {target}")
                break

if __name__ == "__main__":
    main()