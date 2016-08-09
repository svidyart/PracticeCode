class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if(not nums):
            return 0
        l = len(nums)
        if(val not in nums):
            return l
        m = max(nums)+1
        while(True):
            if(val in nums):
                nums[nums.index(val)] = m+1
                l -= 1
            else:
                nums.sort()
                return l
            
            
        