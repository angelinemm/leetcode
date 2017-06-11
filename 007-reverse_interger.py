MIN_INT = -2147483648
MAX_INT = 2147483647


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        x = str(x)
        neg = False
        if x[0] == '-':
            neg = True
            x = x[1:]
        x = x[::-1]
        if neg:
            x = '-' + x
        res = int(x)
        if res < MIN_INT or res > MAX_INT:
            return 0
        return res
