def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    if x < 0:
        return False
    else:
        return int(str(x)[::-1]) == x
