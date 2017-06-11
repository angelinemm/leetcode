class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = {}
        for idx, num in enumerate(nums):
            if num not in my_dict:
                my_dict[num] = [idx]
            else:
                my_dict[num] += [idx]

        if target % 2 == 0:
            half = target / 2
            if len(my_dict.get(half, [])) >= 2:
                return [my_dict[half][0], my_dict[half][1]]

        for num in my_dict:
            other_num = target - num
            if other_num == num:
                return [my_dict[num][0], my_dict[num][0]]
            if other_num in my_dict:
                return [my_dict[num][0], my_dict[other_num][0]]
