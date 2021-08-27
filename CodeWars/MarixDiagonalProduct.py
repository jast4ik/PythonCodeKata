"""
https://www.codewars.com/kata/590bb735517888ae6b000012/train/python
"""

import math


def rotate_matrix_90(m: list, times=1):
    rotated = m.copy()
    for i in range(times):
        rotated = list(zip(*rotated))[::-1]
    return rotated


def get_diag_sum(m: list):
    diag = [[m[i][i + j] for i in range(len(m) - j)] for j in range(1, len(m))]
    diag += [[m[i + j][i] for i in range(len(m) - j)] for j in range(len(m))]
    return sum([math.prod(c_diag) for c_diag in diag])


def sum_prod_diags(matrix):
    sum1 = get_diag_sum(matrix)
    matrix = rotate_matrix_90(matrix, 3)
    sum2 = get_diag_sum(matrix)

    return sum1 - sum2


if __name__ == "__main__":
    M1 = [[1,   4,  7,  6,  5],
          [-3,  2,  8,  1,  3],
          [6,   2,  9,  7,  -4],
          [1,   -2, 4,  -2, 6],
          [3,   2,  2,  -4, 7]]

    sum_prod_diags(M1)
