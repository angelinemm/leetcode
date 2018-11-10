class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        prev = [triangle[0][0]]
        for level, layer in enumerate(triangle[1:]):
            level += 1  # because we started at 1
            layer_size = len(layer)
            curr = []
            for idx, item in enumerate(layer):
                if idx == 0:
                    curr.append(prev[0] + layer[0])
                elif idx < layer_size - 1:
                    curr.append(min(
                        prev[idx-1] + layer[idx],
                        prev[idx] + layer[idx],
                    ))
                else:
                    curr.append(prev[idx-1] + layer[idx])
            prev = curr
        return min(prev)
