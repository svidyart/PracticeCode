class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(s is None):
            return 0
        l = len(s)
        si = 0
        a = ord('A')
        s = s[::-1]
        for i in range(len(s)):
            si += (26**i)*(ord(s[i])-a+1)
        return si
        