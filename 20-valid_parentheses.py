class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening_chars = ('(', '[', '{')
        correct_closing = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        opened = []
        for char in s:
            if char in opening_chars:
                opened += [char]
            else:
                if not opened:
                    return False
                to_be_closed = opened[-1]
                if char == correct_closing[to_be_closed]:
                    opened = opened[:-1]
                else:
                    return False
        return not opened
