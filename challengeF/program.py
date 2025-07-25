#!/usr/bin/env python3

import sys

# read the matrix and return it to main
def read_matrix() -> tuple[list[list[int]], int, int]:
    # read m and n values, check for EOF
    line = sys.stdin.readline().strip()
    if not line:
        return None, -1, -1

    # read m and n values
    m, n = map(int, line.split())

    # read lines of matrix
    return [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)], m, n

# find the minimum path from first column to last
def find_min_path(matrix: list[list[int]], m: int, n: int) -> tuple[int, list[list[int]], list[list[int]]]:
    # initialize dynamic programming matrix with 0s
    dp = [[0] * n for _ in range(m)]

    # initialize a path tracking matrix
    path_track = [[-1] * n for _ in range(m)]

    # initialize first column of dp matrix
    for i in range(m):
        dp[i][0] = matrix[i][0]

    # loop through rest of dp matrix and initialize values based on previous options
    for j in range(1, n):
        for i in range(m):
            # determing row values of options
            up   = m - 1 if i - 1 < 0 else i - 1
            same = i
            down = 0 if i + 1 > m - 1 else i + 1

            # create list of option tuples containing dp values and the rows
            options = [(dp[up][j - 1], up),
                (dp[i][j - 1], same), 
                (dp[down][j - 1], down)
            ]

            # find min of options and store values for assignment
            cost, row = min(options)

            # assign new values of cells
            dp[i][j]         = matrix[i][j] + cost
            path_track[i][j] = row

    # return the min path total cost found in last column
    return min(dp[i][n - 1] for i in range(m)), dp, path_track

# construct the path in reverse by following path_track matrix
def construct_path(dp: list[list[int]], path_track: list[list[int]], m: int, n: int) -> list[int]:
    # loop through rows last column, choose min row for first addition to path
    end_row = min(range(m), key=lambda i: dp[i][n - 1])
    path = []
    col = n - 1
    row = end_row

    # reverse loop through matrix
    while col >= 0:
        # append each row, but add 1 for indexing
        path.append(row + 1)

        # next row is current cell
        row = path_track[row][col]
        col -= 1

    # reverse the path
    path.reverse()

    return path

# main driver
def main():
    while True:
        # read the matrix and check if end of input
        matrix, m , n = read_matrix()
        if not matrix:
            break

        # find the min cost and set the path_track matrix
        min_total_cost, dp, path_track = find_min_path(matrix, m, n)

        # use the path_track matrix to find the path taken in terms of rows used
        path = construct_path(dp, path_track, m, n)

        # print statements
        print(min_total_cost)
        print(' '.join(list(map(str, path))))



if __name__ == "__main__":
    main()