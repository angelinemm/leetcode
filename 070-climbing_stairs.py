class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = {
            1: 1,
            2: 2,
        }
        for step in range(3, n + 1):
            ways[step] = ways[step-1] + ways[step-2]

        return ways[n]
