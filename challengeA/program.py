#!/usr/bin/env python3

import sys

def num_views(heights: list[int]) -> int:
    num_builds = 1
    max_height = heights[0]

    for build in heights[1:]:
        if build > max_height:
            max_height = build
            num_builds += 1

    return num_builds

def main():
    while True:
        line    = sys.stdin.readline().strip()
        if not line:
            break
        heights = list(map(int, line.split()))
        print(num_views(heights[::-1]))



if __name__ == "__main__":
    main()