class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ctr = 0
        ptr = 0
        l = len(nums)
        if(nums == [0]*(l)):
            return
        while(True):
            if(nums[ptr]==0):
                nums.pop(ptr)
                l -= 1
                ctr += 1
            else:    
                ptr += 1
            if(ptr >= l):
                break
        nums.extend([0]*ctr)
        