def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    number = "".join([str(digit) for digit in digits])
    number = str(int(number) + 1)
    number = [int(digit) for digit in number]
    return number


print(plusOne([1, 2, 4, 9, 9]))
