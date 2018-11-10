class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        characters_mapping = {}
        for idx, char in enumerate(s):
            equi_char = t[idx]
            if char in characters_mapping and equi_char != characters_mapping[char]:
                return False
            if char not in characters_mapping and equi_char in characters_mapping.values():
                return False
            characters_mapping[char] = equi_char
        return True
