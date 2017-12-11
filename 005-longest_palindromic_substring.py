class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        if n == 0:
            return None

        if n == 1:
            return s

        best_candidate = s[:2] if (s[0] == s[1]) else s[0]
        up_until_now = len(best_candidate)

        for i in range(2, n):
            # 2 candidates:
            # palindrome ending in i of length up_until_now + 2
            if i - up_until_now - 1 >= 0 and self.isPalindrome(s[i-up_until_now-1:i+1]):
                best_candidate = s[i-up_until_now-1:i+1]
                up_until_now = len(best_candidate)
                continue
            # or palindrome ending in i of length up_until_now + 1
            if i - up_until_now >= 0 and self.isPalindrome(s[i-up_until_now:i+1]):
                best_candidate = s[i-up_until_now:i+1]
                up_until_now = len(best_candidate)

        return best_candidate

    def isPalindrome(self, s):
        return s == s[::-1]
