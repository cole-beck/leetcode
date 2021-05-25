def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # Solution 1 - Complement and extra comparison
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         complement = target - nums[i]
    #         if complement == nums[j] and i != j:
    #             return [i, j]
    
    # Solution 2 - Complement and minus one comparison
    # for i in range(len(nums)):
    #     for j in range((i + 1), len(nums)):
    #         complement = target - nums[i]
    #         if complement == nums[j]:
    #             return [i, j]

    # Solution 3 - No complement var and one comparison
    for i in range(len(nums)):
        for j in range((i + 1), len(nums)):
            if target - nums[i] == nums[j]:
                return [i, j]