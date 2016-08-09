# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(not root):
            return 0
        if(not root.left and not root.right):
            return 1
        if(not root.left):
            return (self.maxDepth(root.right)+1)
        elif(not root.right):
            return (self.maxDepth(root.left)+1)
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
            