import sys


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _isValidBST(self, root, _min=-sys.maxint, _max=sys.maxint):
        if not root:
            return True
        return (
            root.val > _min and
            root.val < _max and
            self._isValidBST(root.left, _min, root.val) and
            self._isValidBST(root.right, root.val, _max)
        )

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._isValidBST(root)
