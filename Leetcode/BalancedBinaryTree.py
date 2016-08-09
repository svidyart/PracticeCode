# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root is None):
            return True
        val = self.depth(root)
        print val
        if(val == False):
            return False
        else:
            return True
            
    def depth(self, root):
        if(root.left is None):
            de_l = 0
        else:
            de_l = self.depth(root.left)
            if(de_l) == False:
                return False
        if(root.right is None):
            de_r = 0
        else:
            de_r = self.depth(root.right)
            if(de_r) == False:
                return False
        #print abs(de_r-de_l) 
        if(abs(de_r-de_l)>1):
            return False
        else:
            return max(de_l, de_r)+1
            