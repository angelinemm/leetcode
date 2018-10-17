class Solution(object):
    def _to_ip_format(self, _int):
        res = []
        for i in range(3, -1, -1):
            item = _int // (3**i)
            res.append(item)
            _int -= item * (3**i)
        return map(lambda x: x+1, res)

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        size = len(s)
        res = []
        for i in range(0, 81):
            _format = self._to_ip_format(i)
            if sum(_format) != size:
                continue
            ip_addr = []
            start = end = 0
            for x in range(0, 4):
                start = end
                end = start + _format[x]
                item = s[start:end]
                if int(item) > 255 or (item.startswith('0') and not item == '0'):
                    ip_addr = []
                    break
                ip_addr += [item]
            if ip_addr:
                res += ['.'.join(ip_addr)]
        return list(set(res))


def main():
    s = Solution().restoreIpAddresses("25525511135")
    print(s)


if __name__ == "__main__":
    main()
