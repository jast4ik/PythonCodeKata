"""Exercises from www.w3resource.com
https://www.w3resource.com/python-exercises/numpy/index-array.php
"""


import numpy as np


if __name__ == "__main__":
    print("\n001. Write a NumPy program to print the NumPy version in your system.")
    print(np.__version__)

    print("\n002. Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array.")
    python_list = [1, 2, 3, 3.56, 8.99, -2.76]
    numpy_list = np.array(python_list)
    print(str(numpy_list))

    print("\n003. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.")
    numpy_list = np.arange(2, 11).reshape(3, 3)
    print(str(numpy_list))

    print("\n004. Write a NumPy program to create a null vector of size 10 and update sixth value to 11.")
    numpy_list = np.zeros(10)
    numpy_list[6] = 11
    print(str(numpy_list))

    print("\n005. Write a NumPy program to create an array with values ranging from 12 to 38.")
    numpy_list = np.arange(12, 39)
    print(str(numpy_list))

    print("\n006. Write a NumPy program to reverse an array (first element becomes last).")
    numpy_list = numpy_list[::-1]
    print(str(numpy_list))

    print("\n007. Write a NumPy program to convert an array to a float type.")
    numpy_list = np.asfarray(numpy_list)
    print(str(numpy_list))

    print("\n 008. Write a NumPy program to create a 2d array with 1 on the border and 0 inside.")
    numpy_list = np.ones((5, 5))
    numpy_list[1:-1, 1:-1] = 0
    print(str(numpy_list))

    print("\n009.  Write a NumPy program to add a border (filled with 0's) around an existing array.")
    numpy_list = np.pad(numpy_list, pad_width=1, mode='constant', constant_values=0.0)
    print(str(numpy_list))

    print("\n010. Write a NumPy program to create a 8x8 matrix and fill it with a checkerboard pattern.")
    numpy_list = np.zeros((8, 8))
    numpy_list[1::2, ::2] = 1
    numpy_list[::2, 1::2] = 1
    print(str(numpy_list))








