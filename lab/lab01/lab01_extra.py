"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    "*** YOUR CODE HERE ***"
    prod=n
    if k==0:
        return 1
    else:
        while k>1:
            prod=prod*(n-1)
            n=n-1
            k=k-1
        return prod


def double_eights(n):

    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    while n>0:
        if n%10==8:
            n=n//10
            if n>0:
                if n%10==8:
                    return True
                else:
                    n=n//10
            else:
                return False
        else:
            n=n//10
    if n==0:
        return False
