class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        newTail = 0
        for idx in range(0, n):
            if nums[idx] != val:
                nums[newTail] = nums[idx]
                newTail += 1
        return newTail
