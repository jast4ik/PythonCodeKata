"""Exercises from www.w3resource.com
https://www.w3resource.com/python-exercises/numpy/index-array.php
"""

import numpy as np

if __name__ == "__main__":
    print("\n001. Write a NumPy program to print the NumPy version in your system.")
    print(np.__version__)

    print("\n002. Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array.")
    python_list = [1, 2, 3, 3.56, 8.99, -2.76]
    numpy_array_1 = np.array(python_list)
    print(str(numpy_array_1))

    print("\n003. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.")
    numpy_array_1 = np.arange(2, 11).reshape(3, 3)
    print(str(numpy_array_1))

    print("\n004. Write a NumPy program to create a null vector of size 10 and update sixth value to 11.")
    numpy_array_1 = np.zeros(10)
    numpy_array_1[6] = 11
    print(str(numpy_array_1))

    print("\n005. Write a NumPy program to create an array with values ranging from 12 to 38.")
    numpy_array_1 = np.arange(12, 39)
    print(str(numpy_array_1))

    print("\n006. Write a NumPy program to reverse an array (first element becomes last).")
    numpy_array_1 = numpy_array_1[::-1]
    print(str(numpy_array_1))

    print("\n007. Write a NumPy program to convert an array to a float type.")
    numpy_array_1 = np.asfarray(numpy_array_1)
    print(str(numpy_array_1))

    print("\n 008. Write a NumPy program to create a 2d array with 1 on the border and 0 inside.")
    numpy_array_1 = np.ones((5, 5))
    numpy_array_1[1:-1, 1:-1] = 0
    print(str(numpy_array_1))

    print("\n009.  Write a NumPy program to add a border (filled with 0's) around an existing array.")
    numpy_array_1 = np.pad(numpy_array_1, pad_width=1, mode='constant', constant_values=0.0)
    print(str(numpy_array_1))

    print("\n010. Write a NumPy program to create a 8x8 matrix and fill it with a checkerboard pattern.")
    numpy_array_1 = np.zeros((8, 8))
    numpy_array_1[1::2, ::2] = 1
    numpy_array_1[::2, 1::2] = 1
    print(str(numpy_array_1))

    print("\n011 Write a NumPy program to convert a list and tuple into arrays.")
    numpy_array_1 = np.array([1, 2, 3, 4, 5, 6])
    print(str(numpy_array_1))
    numpy_array_1 = np.array(((1, 2, 3), (4, 5, 6)))
    print(str(numpy_array_1))

    print("\n012 Write a NumPy program to append values to the end of an array.")
    numpy_array_1 = np.arange(3)
    numpy_array_1 = np.append(numpy_array_1, [[3, 4, 5], [6, 7, 8]])
    numpy_array_1 = np.reshape(numpy_array_1, (3, 3))
    print(str(numpy_array_1))

    print("\n013 Write a NumPy program to create an empty and a full array.")
    numpy_array_1 = np.empty((3, 3))
    print(str(numpy_array_1))
    numpy_array_1 = np.full((3, 3), 3.14)
    print(str(numpy_array_1))

    print("\n014 Write a NumPy program to convert the values of Centigrade degrees into Fahrenheit degrees. \n"
          "Centigrade values are stored into a NumPy array.")
    numpy_array_1 = np.array([-12, 3, 0, 44])
    numpy_array_1 = np.around(numpy_array_1 * 5 / 9 - 160 / 9, decimals=1)
    print(str(numpy_array_1))

    print("\n015 Write a NumPy program to find the real and imaginary parts of an array of complex numbers.")
    numpy_array_1 = np.ones((2, 3), dtype=complex)
    print("Original:\n{}".format(str(numpy_array_1)))
    print("Real part:\n{}".format(str(numpy_array_1.real)))
    print("Imaginary part:\n{}".format(str(numpy_array_1.imag)))

    print("\n016 Write a NumPy program to find the number of elements of an array, \n"
          "length of one array element in bytes and total bytes consumed by the elements.")
    print("Size is:\t{}\nLength of element in bytes:\t{}\nTotal bytes:\t{}".format(
        numpy_array_1.size, numpy_array_1.itemsize, numpy_array_1.nbytes
    ))

    print("\n017 Write a NumPy program to test whether each element of a 1-D array is also present in a second array.")
    numpy_array_1 = np.array([1, 2, 3, 4, 5, 5, 2])
    print(np.in1d([1, 2, 88], numpy_array_1))

    print("\n018 Write a NumPy program to find common values between two arrays.")
    print(np.intersect1d([1, 2, 88], numpy_array_1))

    print("\n019 Write a NumPy program to get the unique elements of an array.")
    print(numpy_array_1)
    print(np.unique(numpy_array_1))

    print("\n020 Write a NumPy program to find the set difference of two arrays. \n"
          "The set difference will return the sorted, unique values in array1 that are not in array2.")
    print(str(numpy_array_1) + " " + str([5, 3, 1]))
    print(np.setdiff1d(numpy_array_1, [5, 3, 1]))

    print("\n021 Write a NumPy program to find the set exclusive-or of two arrays. Set exclusive-or will return \n"
          "the sorted, unique values that are in only one (not both) of the input arrays")
    print(str(numpy_array_1) + " " + str([5, 3, 1, 2]))
    print(np.setxor1d(numpy_array_1, [5, 3, 1, 2]))

    print("\n022 Write a NumPy program to find the union of two arrays. Union will return the unique, \n"
          "sorted array of values that are in either of the two input arrays.")
    print(str(numpy_array_1) + " " + str([5, 3, 1, 2]))
    print(np.union1d(numpy_array_1, [5, 3, 1, 2]))

    print("\n023 Write a NumPy program to test whether all elements in an array evaluate to True.")
    numpy_array_1 = np.array([1, 2, -9, 0])
    print("{} -> {}".format(str(numpy_array_1), str(np.all(numpy_array_1))))

    print("\n024 Write a NumPy program to test whether any array element along a given axis evaluates to True.")
    print("{} -> {}".format(str(numpy_array_1), str(np.any(numpy_array_1))))

    print("\n025 Write a NumPy program to construct an array by repeating. ")
    print("{} -> {}".format(str(numpy_array_1), str(np.tile(numpy_array_1, 2))))

    print("\n026 Write a NumPy program to repeat elements of an array.")
    numpy_array_1 = np.zeros((5, 5))
    numpy_array_1[1::4, ::4] = 1
    numpy_array_1[::4, 1::4] = 3
    print("{} -> {}".format(str(numpy_array_1), str(np.repeat(numpy_array_1, 2))))

    print("\n027 Write a NumPy program to find the indices of the maximum and minimum values along \n"
          "the given axis of an array. ")
    numpy_array_1 = np.array([3, 1, 5, 7, 99, 11])
    print("{} -> index of max: {}. index of min: {}."
          .format(str(numpy_array_1), str(np.argmax(numpy_array_1)), str(np.argmin(numpy_array_1))))

    print("\n028 Write a NumPy program compare two given arrays.")
    numpy_array_2 = np.array([1, -2, 4, 6, 999, 11])
    print("{} < {}:\t{}".format(str(numpy_array_1), str(numpy_array_2), str(np.less(numpy_array_1, numpy_array_2))))
    print("{} <= {}:\t{}".format(
        str(numpy_array_1), str(numpy_array_2), str(np.less_equal(numpy_array_1, numpy_array_2))
    ))
    print("{} == {}:\t{}".format(
        str(numpy_array_1), str(numpy_array_2), str(np.equal(numpy_array_1, numpy_array_2))
    ))
    print("{} > {}:\t{}".format(
        str(numpy_array_1), str(numpy_array_2), str(np.greater(numpy_array_1, numpy_array_2))
    ))
    print("{} >= {}:\t{}".format(
        str(numpy_array_1), str(numpy_array_2), str(np.greater_equal(numpy_array_1, numpy_array_2))
    ))

    print("\n029 Write a NumPy program to sort an along the first, last axis of an array.")
    numpy_array_1 = np.array([3, 565, 24, 76, -1, -676, 98, 0, -2]).reshape(3, 3)
    print("{}\nAxis 0:\n{}\nAxis 1:\n{}".format(
        str(numpy_array_1),
        str(np.sort(numpy_array_1, axis=0)),
        str(np.sort(numpy_array_1, axis=1))))

    print("\n030 Write a NumPy program to sort pairs of first name and last name return their indices.\n"
          "(first by last name, then by first name).")
    numpy_array_1 = ("Fff", "Aaa", "Kkk")
    numpy_array_2 = ("Ggg", "Lll", "Qqq")
    print("{} {}\n{}".format(
        str(numpy_array_1),
        str(numpy_array_2),
        str(np.lexsort((numpy_array_2, numpy_array_1)))
    ))
