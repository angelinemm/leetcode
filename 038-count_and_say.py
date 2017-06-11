class Solution(object):
    def say(self, _str):
        res = ""
        idx = 0
        while idx < len(_str):
            digit = _str[idx]
            count = 0
            while idx < len(_str) and _str[idx] == digit:
                count += 1
                idx += 1
            res += str(count) + str(digit)
        return res

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        return self.say(self.countAndSay(n - 1))
