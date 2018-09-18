def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    final_string = ""
    total_length = len(strs)

    for i in zip(*strs):
        a = i[0]
        if i.count(a) == total_length:
            final_string += a
        else:
            return final_string
    return final_string


print(longestCommonPrefix(['flow', 'flowers', 'flowning', "fl"]))
