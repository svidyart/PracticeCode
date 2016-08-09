# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        #print root
        self.stack = []
        if(root is not None):
            self.current = root
        else:
            return None
        self.stack.append(self.current)
        self.load_stack()
        
    def load_stack(self):
        self.current = self.stack[-1]
        while(self.current.left is not None):
            self.stack.append(self.current.left)
            self.current = self.current.left
        #self.print_stack()
        
    def print_stack(self):
        for i in range(1,len(self.stack)+1):
            print self.stack[-i].val
   
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0
            
    def next(self):
        """
        :rtype: int
        """
        self.nxt = self.stack.pop()
        #print self.nxt
        if(self.nxt.right is not None):
            self.stack.append(self.nxt.right)
            self.load_stack()
        return self.nxt.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())