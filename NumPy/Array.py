"""Exercises from www.w3resource.com
https://www.w3resource.com/python-exercises/numpy/index-array.php
"""


import numpy as np


if __name__ == "__main__":
    print("\n001. Write a NumPy program to print the NumPy version in your system.")
    print(np.__version__)

    print("\n002. Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array.")
    python_list = [1, 2, 3, 3.56, 8.99, -2.76]
    numpy_array = np.array(python_list)
    print(str(numpy_array))

    print("\n003. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.")
    numpy_array = np.arange(2, 11).reshape(3, 3)
    print(str(numpy_array))

    print("\n004. Write a NumPy program to create a null vector of size 10 and update sixth value to 11.")
    numpy_array = np.zeros(10)
    numpy_array[6] = 11
    print(str(numpy_array))

    print("\n005. Write a NumPy program to create an array with values ranging from 12 to 38.")
    numpy_array = np.arange(12, 39)
    print(str(numpy_array))

    print("\n006. Write a NumPy program to reverse an array (first element becomes last).")
    numpy_array = numpy_array[::-1]
    print(str(numpy_array))

    print("\n007. Write a NumPy program to convert an array to a float type.")
    numpy_array = np.asfarray(numpy_array)
    print(str(numpy_array))

    print("\n 008. Write a NumPy program to create a 2d array with 1 on the border and 0 inside.")
    numpy_array = np.ones((5, 5))
    numpy_array[1:-1, 1:-1] = 0
    print(str(numpy_array))

    print("\n009.  Write a NumPy program to add a border (filled with 0's) around an existing array.")
    numpy_array = np.pad(numpy_array, pad_width=1, mode='constant', constant_values=0.0)
    print(str(numpy_array))

    print("\n010. Write a NumPy program to create a 8x8 matrix and fill it with a checkerboard pattern.")
    numpy_array = np.zeros((8, 8))
    numpy_array[1::2, ::2] = 1
    numpy_array[::2, 1::2] = 1
    print(str(numpy_array))

    print("\n011 Write a NumPy program to convert a list and tuple into arrays.")
    numpy_array = np.array([1, 2, 3, 4, 5, 6])
    print(str(numpy_array))
    numpy_array = np.array(((1, 2, 3), (4, 5, 6)))
    print(str(numpy_array))

    print("\n012 Write a NumPy program to append values to the end of an array.")
    numpy_array = np.arange(3)
    numpy_array = np.append(numpy_array, [[3, 4, 5], [6, 7, 8]])
    numpy_array = np.reshape(numpy_array, (3, 3))
    print(str(numpy_array))

    print("\n013 Write a NumPy program to create an empty and a full array.")
    numpy_array = np.empty((3, 3))
    print(str(numpy_array))
    numpy_array = np.full((3, 3), 3.14)
    print(str(numpy_array))

    print("\n014 Write a NumPy program to convert the values of Centigrade degrees into Fahrenheit degrees. \n"
          "Centigrade values are stored into a NumPy array.")
    numpy_array = np.array([-12, 3, 0, 44])
    numpy_array = np.around(numpy_array * 5 / 9 - 160 / 9, decimals=1)
    print(str(numpy_array))

    print("\n015 Write a NumPy program to find the real and imaginary parts of an array of complex numbers.")
    numpy_array = np.ones((2, 3), dtype=complex)
    print("Original:\n{}".format(str(numpy_array)))
    print("Real part:\n{}".format(str(numpy_array.real)))
    print("Imaginary part:\n{}".format(str(numpy_array.imag)))

    print("\n016 Write a NumPy program to find the number of elements of an array, \n"
          "length of one array element in bytes and total bytes consumed by the elements.")
    print("Size is:\t{}\nLength of element in bytes:\t{}\nTotal bytes:\t{}".format(
        numpy_array.size, numpy_array.itemsize, numpy_array.nbytes
    ))

    print("\n017 Write a NumPy program to test whether each element of a 1-D array is also present in a second array.")
    numpy_array = np.array([1, 2, 3, 4, 5, 5, 2])
    print(np.in1d([1, 2, 88], numpy_array))

    print("\n018 Write a NumPy program to find common values between two arrays.")
    print(np.intersect1d([1, 2, 88], numpy_array))

    print("\n019 Write a NumPy program to get the unique elements of an array.")
    print(np.unique(numpy_array))

    print("\n020 Write a NumPy program to find the set difference of two arrays. \n"
          "The set difference will return the sorted, unique values in array1 that are not in array2.")
    print(np.setdiff1d(numpy_array, [5, 3, 1]))


