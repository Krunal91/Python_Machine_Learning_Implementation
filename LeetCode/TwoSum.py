# use dictionary for faster computation

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_dict = {}
    for i in range(len(nums)):

        if nums[i] not in num_dict.keys():
            num_dict[target - nums[i]] = i
        else:
            return [num_dict[nums[i]], i]
