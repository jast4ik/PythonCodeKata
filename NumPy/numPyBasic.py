"""Basic exercises with numpy from
https://www.w3resource.com/python-exercises/numpy/basic/index.php
"""

import numpy as np
import sys


# region ColoredPrint
class CP:
    """Class contains colors and method to use print() with colors"""
    RED = "\033[1;31m"
    YELLOW = '\033[33m'
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
    REVERSE = "\033[;7m"

    @staticmethod
    def print_w_color(input_string='', string_color=RESET):
        """

        :param input_string:
            String to print.
        :param string_color:
            Color from ColoredPrint.
        """
        sys.stdout.write(string_color)
        print(input_string)
        sys.stdout.write(CP.RESET)

    @staticmethod
    def set_stdout_color(stdout_color=RESET):
        sys.stdout.write(stdout_color)

    @staticmethod
    def reset_stdout_color():
        sys.stdout.write(CP.RESET)
# endregion


# region 1. Write a NumPy program to get the numpy version and show numpy build configuration.
def get_numpy_version():
    """Returns numpy version

    :return: str
    """
    return np.__version__


def print_numpy_build_configuration():
    """Prints numpy build configuration"""
    np.show_config()
# endregion


# region 3. Write a NumPy program to test whether none of the elements of a given array is zero.
def does_array_have_zeros(input_array=None, print_array=False):
    """Check if input array have any zeros.

    :param input_array:
        Array that should be checked.
    :param print_array:
        Print input array in answer string - yes or no.
    :return:
        Tuple.
        Boolean - is array contains zeros.
        String - result in natural language.
    """
    return_string = 'Array'
    return_bool = np.all(input_array)

    if print_array:
        return_string += ' ' + str(input_array) + ' '
    else:
        return_string += ' '

    if return_bool:
        return_string += 'does not contain zeros.'
    else:
        return_string += 'contains zeros.'

    return return_bool, return_string
# endregion


# region 4. Write a NumPy program to test whether any of the elements of a given array is non-zero.
def does_array_have_non_zeros(input_array=None, print_array=False):
    """Check if input array have non-zero elements.

    :param input_array:
        Array that should be checked.
    :param print_array:
        Print input array in answer string - yes or no.
    :return:
        Tuple.
        Boolean - is array contains zeros.
        String - result in natural language.
    """
    return_string = 'Array'
    return_bool = np.any(input_array)

    if print_array:
        return_string += ' ' + str(input_array) + ' '
    else:
        return_string += ' '

    if return_bool:
        return_string += 'contains non-zero values.'
    else:
        return_string += 'contains only zeros.'

    return return_bool, return_string
# endregion


# region 5. Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).
def check_array_for_infinite_elements(input_array=None, print_array=False):
    """Check if input array have infinite elements.

        :param input_array:
            Array that should be checked.
        :param print_array:
            Print input array in answer string - yes or no.
        :return:
            Tuple.
            Boolean - is array contains infinite elements.
            String - result in natural language.
        """

    have_infinite_elements = False
    check_list = np.isfinite(input_array)
    infinite_indexes = []

    for index, element in enumerate(check_list):
        if not element:
            infinite_indexes.append(index)
            have_infinite_elements = True

    result_string = 'Array'

    if print_array:
        result_string += ' ' + str(input_array) + ' '
    else:
        result_string += ' '

    if have_infinite_elements:
        result_string += 'have infinite elements at indexes ' + str(infinite_indexes) + '.'
    else:
        result_string += 'does not have any infinite elements.'

    return have_infinite_elements, result_string
# endregion


# region 6. Write a NumPy program to test element-wise for positive or negative infinity.
def check_array_for_infinity_elements(input_array=None, print_array=False):
    """Check if input array have infinity (positive or negative) elements.

            :param input_array:
                Array that should be checked.
            :param print_array:
                Print input array in answer string - yes or no.
            :return:
                Tuple.
                Boolean - is array contains infinity elements.
                String - result in natural language.
            """

    have_infinity_elements = False
    check_list = np.isinf(input_array)
    infinity_indexes = []

    for index, element in enumerate(check_list):
        if element:
            infinity_indexes.append(index)
            have_infinity_elements = True

    result_string = 'Array'

    if print_array:
        result_string += ' ' + str(input_array) + ' '
    else:
        result_string += ' '

    if have_infinity_elements:
        result_string += 'have infinity elements at indexes ' + str(infinity_indexes) + '.'
    else:
        result_string += 'does not have any infinity elements.'

    return have_infinity_elements, result_string
# endregion


# region 7.Write a NumPy program to test element-wise for NaN of a given array.
def check_array_for_nan_elements(input_array=None, print_array=False):
    """Check if input array have NaN elements.

            :param input_array:
                Array that should be checked.
            :param print_array:
                Print input array in answer string - yes or no.
            :return:
                Tuple.
                Boolean - is array contains NaN elements.
                String - result in natural language.
            """

    have_nan_elements = False
    check_list = np.isnan(input_array)
    nan_indexes = []

    for index, element in enumerate(check_list):
        if element:
            nan_indexes.append(index)
            have_nan_elements = True

    result_string = 'Array'

    if print_array:
        result_string += ' ' + str(input_array) + ' '
    else:
        result_string += ' '

    if have_nan_elements:
        result_string += 'have NaN elements at indexes ' + str(nan_indexes) + '.'
    else:
        result_string += 'does not have any NaN elements.'

    return have_nan_elements, result_string
# endregion


# region 8.Write a NumPy program to test element-wise for complex number, real number of a given array.
# Also test whether a given number is a scalar type or not.

# endregion


if __name__ == '__main__':
    # region Exercise 1
    CP.print_w_color('Exercise 1:\n--------------------', CP.GREEN)
    CP.print_w_color('\tnumpy version is:', CP.YELLOW)
    CP.print_w_color('\t\t' + get_numpy_version(), CP.BLUE)
    CP.print_w_color('\tnumpy build configuration:', CP.YELLOW)
    CP.set_stdout_color(CP.BLUE)
    print_numpy_build_configuration()
    CP.reset_stdout_color()
    # endregion
    # region Exercise 2. Write a NumPy program to get the numpy version and show numpy build configuration.
    CP.print_w_color('\nExercise 2:\n--------------------', CP.GREEN)
    CP.set_stdout_color(CP.BLUE)
    print(np.info(np.add))
    CP.reset_stdout_color()
    # endregion
    # region Exercise 3.
    list_with_zeros = [1, 3, 6, 8, 9, 0]
    list_without_zeros = [1, 3, 6, 8, 9]
    CP.print_w_color('\nExercise 3:\n--------------------', CP.GREEN)
    CP.print_w_color('\t' + does_array_have_zeros(list_without_zeros, True)[1], CP.BLUE)
    CP.print_w_color('\t' + does_array_have_zeros(list_with_zeros, True)[1], CP.BLUE)
    # endregion
    # region Exercise 4.
    list_all_zeros = [0, 0, 0]
    CP.print_w_color('\nExercise 4:\n--------------------', CP.GREEN)
    CP.print_w_color('\t' + does_array_have_non_zeros(list_with_zeros, True)[1], CP.BLUE)
    CP.print_w_color('\t' + does_array_have_non_zeros(list_all_zeros, True)[1], CP.BLUE)
    # endregion
    # region Exercise 5.
    CP.print_w_color('\nExercise 5:\n--------------------', CP.GREEN)
    list_with_inf = np.array([np.nan, 3, 6, 8, np.inf])
    list_without_inf = np.array([1, 2, 6, 8])
    CP.print_w_color('\t' + check_array_for_infinite_elements(list_with_inf, True)[1], CP.BLUE)
    CP.print_w_color('\t' + check_array_for_infinite_elements(list_without_inf, True)[1], CP.BLUE)
    # endregion
    # region Exercise 6.
    CP.print_w_color('\nExercise 6:\n--------------------', CP.GREEN)
    list_with_inf = np.array([np.nan, 3, 6, 8, np.inf, 77, -np.inf])
    CP.print_w_color('\t' + check_array_for_infinity_elements(list_with_inf, True)[1], CP.BLUE)
    CP.print_w_color('\t' + check_array_for_infinity_elements(list_without_inf, True)[1], CP.BLUE)
    # endregion
    # region Exercise 7.
    CP.print_w_color('\nExercise 7:\n--------------------', CP.GREEN)
    list_with_nan = np.array([np.nan, 3, 6, 8, np.inf, 77, np.nan])
    CP.print_w_color('\t' + check_array_for_nan_elements(list_with_nan, True)[1], CP.BLUE)
    CP.print_w_color('\t' + check_array_for_nan_elements(list_without_inf, True)[1], CP.BLUE)
    # endregion

