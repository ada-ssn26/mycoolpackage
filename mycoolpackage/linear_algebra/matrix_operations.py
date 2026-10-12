import numpy as np

def matrix_addition(matrix1, matrix2):
    """Add two same-shaped arrays element-wise.

    Parameters
    ----------
    matrix1 : numpy.ndarray
        First input array.
    matrix2 : numpy.ndarray
        Second input array. It must have the same shape as ``matrix1``.

    Returns
    -------
    numpy.ndarray
        Element-wise sum of the input arrays.

    Raises
    ------
    ValueError
        If the input arrays do not have the same shape.
    """
    if matrix1.shape != matrix2.shape:
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    return np.add(matrix1, matrix2)
