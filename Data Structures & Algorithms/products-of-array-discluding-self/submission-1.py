class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = 1 
        temp = []
        prev = 1
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prev *= nums[i-1]
                prefix.append(prev)
        for j in range(len(nums)-1,-1,-1):
            if j == len(nums)-1:
                temp.append(prefix[j])
                suffix *= nums[j]
            elif j == 0 :
                temp.append(suffix)
            else:
                temp.append(prefix[j]*suffix)
                suffix *= nums[j]


        return temp[::-1]

            
        
        




                
        