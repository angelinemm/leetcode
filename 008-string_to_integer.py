class Solution(object):
    int_max = 2147483647
    int_min = -2147483648

    def myAtoi(self, _str):
        """
        :type str: str
        :rtype: int
        """
        is_negative = False
        _str = _str.strip()

        if not _str:
            return 0

        if _str[0] == '-':
            is_negative = True

        _str = _str[1:] if _str[0] in ('-', '+') else _str
        end = 0
        while end < len(_str) and _str[end].isdigit():
            end += 1

        _str = _str[0:end]
        if not _str:
            return 0

        _str = _str[::-1]

        res = 0
        for idx, digit in enumerate(_str):
            res += (int(digit) * 10 ** idx)

        res = res * -1 if is_negative else res
        res = min(self.int_max, res)
        res = max(self.int_min, res)

        return res
