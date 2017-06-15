class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = max_length = 0
        used_char = {}
        for idx, char in enumerate(s):
            if char in used_char and used_char[char] >= start:
                start = used_char[char] + 1
            else:
                max_length = max(max_length, idx - start + 1)
            used_char[char] = idx

        return max_length
