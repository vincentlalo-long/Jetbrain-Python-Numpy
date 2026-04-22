import numpy as np


def reshape_transpose(start, stop, step=1):
    # Create a 1D array using arange function
    a = np.arange(start, stop, step)
    a = a.reshape(1, a.shape[0])
    # Reshape the 1D array so that you can transpose it
    return a.T# Return the transposed array


if __name__ == '__main__':
    print(reshape_transpose(1, 100, 10))
    print(reshape_transpose(0, 5))
