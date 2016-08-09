# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if(not root):
            return None
        if(not root.left and not root.right):
            return root
        if(not root.left and root.right):
            root.left = self.invertTree(root.right)
            root.right = None
            return root
        elif(not root.right and root.left):
            root.right = self.invertTree(root.left)
            root.left = None
            return root
        else:
            tmp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(tmp)
            return root
            