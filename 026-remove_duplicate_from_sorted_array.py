class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        newTail = 0
        for idx in range(1, n):
            if nums[idx] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[idx]
        return newTail + 1
