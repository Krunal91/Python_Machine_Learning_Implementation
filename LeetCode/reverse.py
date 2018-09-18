def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    n = int(str(abs(x))[::-1])
    if x == 0:
        return 0
    else:
        a = ((x > 0) - (x < 0))
        b = n * (n < 2 ** 31)
        return a * b


reverse(-123)
