# MyCoolPackage

MyCoolPackage is a small Python package of NumPy-based helpers for common
array operations. It currently provides element-wise array addition,
element-wise multiplication, and the mean of all array elements. It is intended
as a lightweight learning project and a simple example of packaging reusable
Python functions.

## Requirements

- Python 3.10 or newer
- NumPy (installed automatically with the package)

## Installation

From the root of a local checkout, install the package with:

```bash
python -m pip install .
```

For development, install the package in editable mode together with the
development tools:

```bash
python -m pip install -e ".[dev]"
```

The distribution is named `cool-package`; import it in Python as
`mycoolpackage`.

## Usage

Each function accepts NumPy arrays. The two element-wise operations require
their input arrays to have the same shape and raise `ValueError` otherwise.

```python
import numpy as np
import mycoolpackage

left = np.array([[1, 2], [3, 4]])
right = np.array([[5, 6], [7, 8]])

sum_array = mycoolpackage.matrix_addition(left, right)
print(sum_array)
# [[ 6  8]
#  [10 12]]

product_array = mycoolpackage.array_multiplication(left, right)
print(product_array)
# [[ 5 12]
#  [21 32]]

average = mycoolpackage.matrix_mean(left)
print(average)
# 2.5
```

`array_multiplication` is element-wise multiplication, not matrix
multiplication. `matrix_mean` computes one mean over all elements in the array.

## Running tests

Install the development tools and run the test suite from the project root:

```bash
python -m pip install -e ".[dev]"
python -m pytest
```