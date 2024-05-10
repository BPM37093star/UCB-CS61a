"""Lab 1: Expressions and Control Structures"""

def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x>0 and y > 0 # You can replace this line!

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    "*** YOUR CODE HERE ***"
    x=0
    y=10**x
    while n/y >=10:
        x=x+1
        y=10**x
    sum_digits=n//y
    while x>0:
        sum_digits=sum_digits+n%y//(10**(x-1))
        x=x-1
        y=10**x
    return sum_digits
