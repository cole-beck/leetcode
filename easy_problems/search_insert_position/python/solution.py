class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Solution 1 - Recursive binary search solution
        return self.searchInsertRecursive(nums, target, 0, len(nums) - 1)


    def searchInsertRecursive(self, nums, target, start, end):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :type end: int
        :rtype: int
        """

        # Base case: Only one element to check
        if start >= end:
            if nums[start] < target:
                return start + 1
            else:
                return start

        # Non-base case
        middle = start + ((end - start) // 2)

        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            return self.searchInsertRecursive(nums, target, middle + 1, end)
        else:
            return self.searchInsertRecursive(nums, target, start, middle - 1)