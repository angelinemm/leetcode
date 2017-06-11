class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numeral = 0
        rom_to_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        idx = len(s) -1
        while idx >=0:
            char = s[idx]
            if idx == 0:
                numeral += rom_to_num[char]
                break
            char_before = s[idx - 1]
            if rom_to_num[char] > rom_to_num[char_before]:
                numeral += rom_to_num[char] - rom_to_num[char_before]
                idx -= 2
                continue
            numeral += rom_to_num[char]
            idx -= 1
        return numeral
