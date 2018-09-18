def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(s) == 1:
        return roman_dict[s]
    total = 0
    for i in range(1, len(s)):
        if roman_dict[s[i - 1]] < roman_dict[s[i]]:
            total -= roman_dict[s[i - 1]]
        else:
            total += roman_dict[s[i - 1]]
    total += roman_dict[s[len(s) - 1]]

    return total


print(romanToInt("III"))
