class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(not s):
            return 0
            
        l = s.strip(' ').split(' ')
        
        return len(l[-1])