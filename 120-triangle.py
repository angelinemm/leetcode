class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = []
        res.append([triangle[0][0]])
        for level, layer in enumerate(triangle[1:]):
            level += 1  # because we started at 1
            layer_size = len(layer)
            res.append([])
            for idx, item in enumerate(layer):
                if idx == 0:
                    res[level].append(res[level-1][0] + layer[0])
                elif idx < layer_size - 1:
                    res[level].append(min(
                        res[level-1][idx-1] + layer[idx],
                        res[level-1][idx] + layer[idx],
                    ))
                else:
                    res[level].append(res[level-1][idx-1] + layer[idx])
        result = min(res[-1])
        return result
