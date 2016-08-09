class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(not s):
            return ''
        return ''.join([s[-i] for i in range(1,len(s)+1)])
    