class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        res = [True] * n
        res[0] = res[1] = False
        for i in xrange(2, n):
            if res[i]:
                for j in xrange(i, n):
                    if i * j > n - 1:
                        break
                    res[i*j] = False
        return sum(res)
