class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ls = []
        self.lq = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.ls.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if(not self.lq):
            while(self.ls):
                self.lq.append(self.ls.pop())
        return self.lq.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if(self.lq):
            return self.lq[-1]
        elif(self.ls):
            while(self.ls):
                self.lq.append(self.ls.pop())
            return self.lq[-1]
        else:
            return None
        

    def empty(self):
        """
        :rtype: bool
        """
        if(not self.lq and not self.ls):
            return True
        else:
            return False
        