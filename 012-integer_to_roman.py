class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ""
        num_to_rom = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
        }
        for _num in sorted(num_to_rom.keys(), reverse=True):
            factor = num / _num
            if factor:
                roman += num_to_rom[_num] * factor
                num -= factor * _num

        roman = roman.replace('VIIII', 'IX')
        roman = roman.replace('IIII', 'IV')
        roman = roman.replace('LXXXX', 'XC')
        roman = roman.replace('XXXX', 'XL')
        roman = roman.replace('XXXXXX', 'LX')
        roman = roman.replace('DCCCC', 'CM')
        roman = roman.replace('CCCC', 'CD')

        return roman
