from sq_calc import ft_square
import pytest


def main():
    test1_ft_square()


def test1_ft_square():
    try:
        assert ft_square(1) == 1
        assert ft_square(0) == 0
        assert ft_square(-1) == 1
    except AssertionError:
        print(" A test is failing")


if __name__ == '__main__':
    main()
