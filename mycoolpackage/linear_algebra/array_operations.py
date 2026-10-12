import numpy as np


def array_multiplication(matrix1, matrix2):
    """Multiply two same-shaped arrays element-wise.

    This performs element-wise multiplication, not matrix multiplication.

    Parameters
    ----------
    matrix1 : numpy.ndarray
        First input array.
    matrix2 : numpy.ndarray
        Second input array. It must have the same shape as ``matrix1``.

    Returns
    -------
    numpy.ndarray
        Element-wise product of the input arrays.

    Raises
    ------
    ValueError
        If the input arrays do not have the same shape.
    """
    if matrix1.shape != matrix2.shape:
        raise ValueError(
            "Matrices must have the same dimensions for multiplication."
            )

    return np.multiply(matrix1, matrix2)
