class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        l = 0
        i = 0
        j = i+1
        while(j < len(nums)):
            if(nums[i]==nums[j]):
                j+=1
                continue
            nums[l] = nums[i]
            i = j
            j = i + 1
            l += 1
        nums[l] = nums[i]
        return l+1
        