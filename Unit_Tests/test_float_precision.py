from sq_calc import ft_square
import pytest


# THIS FIRST TEST must FAIL because there is no exact float that gives us
# 2 when squared, so the value will never be equal to the exact float 2.0
def test_float_sq():
    assert ft_square(1.414213562373095048801688724208) == 2


# That's why we better use the approximation when it comes to infinite floats
def test_float_approx_sq():
    assert ft_square(1.414213562373095048801688724208) == pytest.approx(2)


# We can play with th proximity range:
#Notice how precise we can go:
def test_float_approx_sq1():
    assert ft_square(1.414213562373095048801688724208) == pytest.approx(2, abs=5e-16)
# Here is the number we get is greater or less then the value we put
# with 0.0000000000000005 it's going to be tolerated and considered as right


# Here we narrowed the tolerance range to 0.0000000000000001
# So in this case it must not pass
def test_float_approx_sq2():
    assert ft_square(1.414213562373095048801688724208) == pytest.approx(2, abs=1e-16)


# Well Here I only tried to demostrate how the floats precision testing work
# But ofcourse in real life scenarios we will need it in case we want 
# somehow to optimize the precision of our returned vaklues