def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    counter = 0
    change = nums[0]
    for i in range(1, len(nums)):
        if change != nums[i]:
            counter += 1
            nums[counter] = nums[i]
            change = nums[i]
    nums = nums[:counter]
    return counter


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
