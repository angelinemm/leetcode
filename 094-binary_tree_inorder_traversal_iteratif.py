# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        to_do = []
        current = root
        while current or to_do:
            if current:
                to_do.append(current)
                current = current.left
            else:
                temp = to_do.pop()
                res.append(temp.val)
                current = temp.right
        return res
