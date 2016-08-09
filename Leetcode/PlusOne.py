class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if(not digits):
            return [1]
        i = 0
        while(True):
            i += 1
            if(i > len(digits)):
                digits.insert(0,1)
                return digits            
            digits[-i] = digits[-i] + 1
            if(digits[-i]>=10):
                digits[-i] %= 10
            else:
                return digits
        