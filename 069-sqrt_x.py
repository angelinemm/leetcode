class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        _int = 2
        while _int * _int < x:
            _int *= 2

        if _int * _int == x:
            return _int

        _int1 = _int/2
        _int2 = _int
        while _int2 - _int1 > 1:
            half = _int1 + (_int2 - _int1) // 2
            square = half * half
            if square == x:
                return half
            if square > x:
                _int2 = half
            if square < x:
                _int1 = half

        return _int1
