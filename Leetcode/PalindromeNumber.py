class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0 ):
            return False
        if(x < 10):
            return True
        n = 1
        while(True):
            if(int(x/10**n)>0):
                n+=1
            else:
                break
        return (self.revNumber(x,n)==x)
    
    def revNumber(self, x, n):
        k = x
        temp = 0
        while(k>0):
            temp *= 10
            temp += (k%10)
            k /= 10
        return temp