class Solution(object):
    def lengthOfLastWord(self, s):
            """
            :type s: str
            :rtype: int
            """
            if not s:
                return 0
            phrase = s.strip(' ').split(' ')
            return len(phrase[-1])
