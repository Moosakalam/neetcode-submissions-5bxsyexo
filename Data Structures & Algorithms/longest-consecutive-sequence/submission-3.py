class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        curr = 1 
        new = 0 
        if len(nums) == 0 :
            return 0 
        for i in range(len(nums)-1):
            if i == 0 :
                curr = 1
                new = 1
            if nums[i+1] == nums[i]+1:
                new +=1
            else:
                new = 1

            if new>curr:
                curr = new 
        return curr

            
        
        