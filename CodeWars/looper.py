"""
https://www.codewars.com/kata/5a35f08b9e5f4923790010dc/train/python
"""

from decimal import Decimal
import numpy as np


def looper(start, stop, number):
    res = [float(start)]
    if number > 1:
        res += np.array([(stop - start) / (number - 1) * i + start for i in range(1, number - 1)],
                        dtype=np.float64).tolist()
        res += [float(stop)]

    return res


if __name__ == "__main__":
    np.set_printoptions(precision=15)
    print(looper(93, 445, 100))

    pass
