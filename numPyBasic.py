"""Basic exercises with numpy from
https://www.w3resource.com/python-exercises/numpy/basic/index.php
"""

import numpy as np


# region 1. Write a NumPy program to get the numpy version and show numpy build configuration
def get_numpy_version():
    """Returns numpy version

    :return: str
    """
    return np.__version__


def get_numpy_build_configuration():
    """Returns numpy build configuration

    :return: str
    """
    return str(np.__config__.show())
# endregion

if __name__ == '__main__':
    # region Exercise 1
    print('Exercise 1:')
    print('\tnumpy version is: \n\t\t' + get_numpy_version())
    print('\tnumpy build configuration:')
    print(get_numpy_build_configuration())
    # endregion
    # region Exercise 2. Write a NumPy program to get the numpy version and show numpy build configuration
    print('Exercise 2:')
    print(np.info(np.add))
    # endregion
