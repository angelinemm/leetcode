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
        if not root:
            return []

        left = self.inorderTraversal(root.left) if root.left else []
        right = self.inorderTraversal(root.right) if root.right else []

        return left + [root.val] + right
