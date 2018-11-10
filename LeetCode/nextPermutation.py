def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if not nums: return -1
    n = len(nums) - 1
    index = 0
    swap = False
    for i in range(n, 0, -1):
        if nums[i - 1] < nums[i]:
            index = i - 1
            break
    for j in range(n, 0, -1):
        if nums[j] > nums[index]:
            nums[index], nums[j] = nums[j], nums[index]
            swap = True
            nums[index + 1:] = nums[index + 1:][::-1]
            break

    if not swap:
        nums[:] = nums[::-1]

    return


print(nextPermutation([1, 2, 3]))
