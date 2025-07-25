#!/usr/bin/env python3

import sys

def find_sum_path(target: int, tree: list[int], curr_index: int, path: list[int], result: list[list[int]]) -> list[list[int]]:
    # null node
    if curr_index >= len(tree) or tree[curr_index] == 0:
        return
    
    # calculate left and right children of current node
    left_child  = 2 * curr_index + 1
    right_child = 2 * curr_index + 2

    # if at a leaf node and target is deplenished
    if target == tree[curr_index] and (
        (left_child >= len(tree) or tree[left_child] == 0) and
        (right_child >= len(tree) or tree[right_child] == 0)
    ):
        result.append(path[:])
        return
    
    # summed too large
    if target < 0:
        return
    
    # run recursion on left and right children
    if left_child < len(tree):
        find_sum_path(target - tree[left_child], tree, left_child, path + [tree[left_child]], result)
    if right_child < len(tree):
        find_sum_path(target - tree[right_child], tree, right_child, path + [tree[right_child]], result)

    return result

def main():
    while True:
        target = sys.stdin.readline().strip()
        if not target:
            break
        target = int(target)
        tree   = list(map(int, sys.stdin.readline().split()))

        if len(tree) == 1:
            if tree[0] == target:
                print(f"{target}: {tree[0]}")
            continue

        paths = find_sum_path(target - tree[0], tree, 0, [tree[0]], [])
        if paths:
            for path in sorted(paths):
                print(f"{target}: {' '.join(list(map(str, path)))}")



if __name__ == "__main__":
    main()