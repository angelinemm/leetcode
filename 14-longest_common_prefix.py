class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        shortest_string_len = min(len(_str) for _str in strs)
        idx = 0
        while idx < shortest_string_len:
            char = strs[0][idx]
            if any(_str[idx] != char for _str in strs):
                break
            idx += 1
        return strs[0][:idx]
