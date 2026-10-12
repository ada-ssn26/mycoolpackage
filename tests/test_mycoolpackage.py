import mycoolpackage

import pytest

import numpy as np

@pytest.mark.parametrize("matrix_a, matrix_b, expected", [
    ([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[6, 8], [10, 12]]),
    ([[0, 0], [0, 0]], [[1, 1], [1, 1]], [[1, 1], [1, 1]]),
    ([[1]], [[2]], [[3]]),
])
def test_matrix_addition(matrix_a, matrix_b, expected):
    result = mycoolpackage.matrix_addition(
        np.array(matrix_a), np.array(matrix_b)
    )
    assert np.array_equal(result, np.array(expected))

@pytest.mark.parametrize("matrix_a, matrix_b, expected", [
    ([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[5, 12], [21, 32]]),
])
def test_array_multiplication(matrix_a, matrix_b, expected):
    result = mycoolpackage.array_multiplication(
        np.array(matrix_a), np.array(matrix_b)
    )
    assert np.array_equal(result, np.array(expected))

@pytest.mark.parametrize("matrix, expected", [
    ([[1, 2], [3, 4]], 2.5),
])
def test_matrix_mean(matrix, expected):
    result = mycoolpackage.matrix_mean(np.array(matrix))
    assert result == expected