"""
https://www.codewars.com/kata/590bb735517888ae6b000012/train/python
"""

import math


def sum_prod_diags(matrix):

    # sum1 = [matrix[i][i + j] for j in range(len(matrix) - 1) for i in range(len(matrix) - j)]
    # sum1 = [matrix[i + j][j] for i in range(1, len(matrix) - 1) for j in range(len(matrix) - i)]
    # sum1 = [matrix[i][i + 3] for i in range(len(matrix) - 3)]
    sum1 = list()
    sum2 = list()

    for index in range(len(matrix) - 1):
        sum1.append([matrix[i][i + index] for i in range(len(matrix) - index)])
    for index in range(1, len(matrix) - 1):
        sum1.append([matrix[i + index][i] for i in range(len(matrix) - index)])

    sum2 = [matrix[i][i - 1] for i in range(1, len(matrix))]

    for i in reversed(range(1, len(matrix))):
        print(i)
    print(sum2)
    return [[]]


if __name__ == "__main__":
    M1 = [[1,   4,  7,  6,  5],
          [-3,  2,  8,  1,  3],
          [6,   2,  9,  7,  -4],
          [1,   -2, 4,  -2, 6],
          [3,   2,  2,  -4, 7]]

    sum_prod_diags(M1)
