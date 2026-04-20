from sq_calc import ft_hello, ft_helo


#Now Let's see some different tests:
#This is a case where we test a function that has no return value
def test_hello():
    # When we have some functions that only apply some sort of side effect
    # But have no return value, it's really hard to test them so we better
    # make them return some valid value then apply the side effects in the main
    # That's just a good behavior to make it testable
    ft_hello('med')

def test_helo():
    assert ft_helo('Med') == 'Hello, Med'
    assert ft_helo() == 'Hello, World'