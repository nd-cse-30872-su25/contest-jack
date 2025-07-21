#!/usr/bin/env python3

import sys

WAYS = [2, 3, 7]

def find_ways_recursive(target_remaining: int, scores: list[int], last_score_index: int, result: list[list[int]]) -> list[list[int]]:
    # there is no more scores needed
    if target_remaining == 0:
        result.append(scores[:])
        return
    
    # target score exceeded
    if target_remaining < 0:
        return

    for i in range(last_score_index, len(WAYS)):
        # append current way to scores in case it will be used
        scores.append(WAYS[i])
        
        # recursive call, making sure to decrement target_remaining and alter last_score_index
        find_ways_recursive(target_remaining - WAYS[i], scores, i, result)

        # allow backtracking
        scores.pop()

    return result

def main():
    while True:
        # read input
        target = sys.stdin.readline().strip()
        if not target:
            break
        target = int(target)

        # run recursion
        solutions = find_ways_recursive(target, [], 0, [])

        # print statement with special case of 1 way to score
        if len(solutions) == 1:
            print(f"There is {len(solutions)} way to achieve a score of {target}:")
        else:
            print(f"There are {len(solutions)} ways to achieve a score of {target}:")

        # print out all of the different ways to score
        for s in solutions:
            print(' '.join(map(str,s)))

if __name__ == "__main__":
    main()