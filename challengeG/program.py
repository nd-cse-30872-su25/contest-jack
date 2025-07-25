#!/usr/bin/env python3

import sys

# parse the adjacency matrix from stdin
def parse_adj_matrix() -> tuple[list[list[int]], int] | None:
    # parse n from input
    line = sys.stdin.readline().strip()

    # stop parsing if at end of input
    if not line:
        return None
    
    # store n value
    n = int(line)

    # collect matrix and return
    matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    return matrix, n

# use dfs search to count number of circuits in adjacency matrix
def num_circuits(matrix: list[list[int]], n: int) -> int:
    # initialize frontier stack, visited set, and circuit counter
    frontier = []
    visited  = set()
    count    = 0

    # loop through possible starting nodes
    for node in range(n):
        # if a node has already been used in a circuit, skip it
        if node in visited:
            continue

        # if a new node has been found, increment count and perform dfs on it
        count += 1
        visited.add(node)
        frontier.append(node)

        # loop while there are nodes on the frontier to be searched
        while frontier:
            # pop current node
            curr = frontier.pop()

            # iterate through possible neighbors
            for neighbor in range(n):
                # if there is a new connection add to visited and frontier to be searched
                if matrix[curr][neighbor] == 1 and not neighbor in visited:
                    visited.add(neighbor)
                    frontier.append(neighbor)

    # return the count of circuits
    return count

# main driver
def main():
    count = 1
    while True:
        # parse adj matrix
        result = parse_adj_matrix()

        # if no more input, break the loop
        if not result:
            break

        # split up tuple returned from parse function
        matrix, n = result

        # call dfs search to determine number of circuits
        print(f"System {count} isolated circuits: {num_circuits(matrix, n)}")

        # iterate system count for printing
        count += 1

if __name__ == "__main__":
    main()