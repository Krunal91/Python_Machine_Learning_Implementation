def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    paren_dict = {'(': ')', '{': '}', '[': ']'}

    stack = []
    if len(s) == 0:
        return True
    if len(s) == 1:
        return False
    if s[0] not in paren_dict.keys():
        return False

    for i in s:
        if i in paren_dict.keys():
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            match = stack.pop()
            if paren_dict[match] == i:
                pass
            else:
                return False
    return True if len(stack) == 0 else False


print(isValid("[])"))
