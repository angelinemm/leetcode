class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or nums[0] >= target:
            return 0
        for idx in range(1, len(nums)):
            if nums[idx] >= target:
                return idx
        return len(nums)
