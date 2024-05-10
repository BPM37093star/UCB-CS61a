""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    i = 1
    num_fac = 0
    while i <= n:
        if n % i == 0:
            num_fac += 1
            i += 1
        else:
            i += 1
    if num_fac == 2:
        return True
    else:
        return False




def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    else:
        if a > b:
            return gcd(b, a % b)
        else:
            return gcd(a, b % a)




def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    elif n >= 10 and n < 100:
        if n // 10 + n % 10 == 10:
            return 1
        else:
            return 0
    else:
        one_digit = n % 10
        ten_pair = 0
        i = n
        while i // 10 > 0:
            ten_digit = i // 10 % 10
            if ten_digit + one_digit == 10:
                ten_pair += 1
            i = i // 10
        return ten_pair + ten_pairs(n // 10)
