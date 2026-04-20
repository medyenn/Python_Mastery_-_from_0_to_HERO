# We have to pip install the library: pytest
# then only we need to do is to define the testing function
# that we want to apply to our code, then run this file with pytest
# NOT: python3 test_file.py,
# INSTEAD we should do this :  pytest test_file.py

# Example: try run this file using: pytest auto_test_sq.py :
from sq_calc import ft_square
import pytest


def test_sq():
    assert ft_square(1) == 1
    assert ft_square(-1) == 1
    assert ft_square(0) == 0
# We notice that it stops at the first bug so we can't really know all the
# buggy cases, that's why we better split cases into categories
# And define a test function for each category

# In these cases we will only test the input cases that we expect to get
def test_positive_sq():
    assert ft_square(2) == 4
    assert ft_square(1) == 1


def test_zero_sq():
    assert ft_square(0) == 0


def test_negative_sq():
    assert ft_square(-1) == 1
    assert ft_square(-2) == 4
# After analyzing the output of : pytest auto_test_sq.py
# you can go ahead and correct ft_square() in the sq_calc.py file
# then rerun the file using pytest


# Now let's test some cases where the input might be not as expected
# Let's see how we can catch errors other than AssertionError:
def test_str_sq():
    with pytest.raises(TypeError):
        ft_square('1')
        # Here we say like:
# If a TypeError was raised in such case considere it OK
