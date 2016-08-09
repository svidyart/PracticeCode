# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if(p is None and q is None):
            return True
        elif(p is None or q is None):
            return False
        if(p.val == q.val):
            if(p.left is not None and q.left is not None):
                temp = self.isSameTree(p.left, q.left)
                if(temp is False):
                    return temp
            elif(p.left is not None or q.left is not None):
                return False
            
            if(p.right is not None and q.right is not None):
                return self.isSameTree(p.right, q.right)
            elif(p.right is not None or q.right is not None):
                return False
            else:
                return True
        else:
            return False
        