class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(not s):
            return 0
        d = {}
        i = 0
        ssmax = 1
        k = 0
        while(True):
            if(s[k] not in d):
                d[s[k]] = k
            else:
                tpos = d[s[k]]
                if(tpos >= i):
                    ssmax = max(ssmax, k-i)
                    i = tpos+1
                d[s[k]] = k
            k +=1
            if(k == len(s)):
                ssmax = max(ssmax, k-i)
                break
        return ssmax
            
            
            
        
        