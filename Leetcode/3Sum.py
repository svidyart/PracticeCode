class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        soln = []
        if(len(nums)<3):
            return []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k = -nums[i]-nums[j]
                if(k in nums[j+1:]):
                    soln.append(sorted((nums[i],nums[j],k)))
                    continue
        return self.unique_solution(soln)
        
    def unique_solution(self,soln):
        new_soln = []
        set_soln = set()
        for i in soln:
            if(tuple(i) in set_soln):
                continue
            else:
                new_soln.append(i)
                set_soln.add(tuple(i))
        return new_soln