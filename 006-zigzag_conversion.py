class Solution(object):
    def convert(self, s, n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s <= 1 or n == 1 or len(s) <= n:
            return s

        per_line = {}
        for idx, char in enumerate(s):
            row = idx % (2*n-2)
            if row >= n:
                row = 2*n - row - 2
            if row not in per_line:
                per_line[row] = ''
            per_line[row] += char

        encoded = ''
        for line in range(0, n):
            encoded += per_line[line]

        return encoded
