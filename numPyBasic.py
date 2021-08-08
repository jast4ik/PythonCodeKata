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
def does_array_have_zeros(input_array=[], print_array=False):
    """Check if input array have any zeros.
    First is boolean, second is string that
    describes result in natural language.

    :param input_array:
        Array that should be checked.
    :param print_array:
        Print array in answer string - tes or no.
    :return:
        Tuple.
        Boolean - is array contains zeros
        String - result in natural language
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
