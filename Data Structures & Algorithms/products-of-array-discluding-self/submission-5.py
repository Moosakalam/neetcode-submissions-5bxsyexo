class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        pre = 1 
        suf = 1
        res= []

        for i in range(len(nums)):
            prefix[i] = pre * prefix[i]
            pre *= nums[i]
        
        for j in range(len(nums)-1,-1,-1):
            
            suffix[j] = suf * suffix[j]
            suf *= nums[j]
        
        for i in range(len(nums)):
            res.append(suffix[i]*prefix[i])
        return(res)
            

