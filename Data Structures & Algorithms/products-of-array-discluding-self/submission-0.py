class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0 
        left = 0 
        right = len(nums) 
        mult = 1
        temp = []
        while i < len(nums):
            if i  == 0 :
                for j in range(i+1,right):
                    mult *= nums[j]
                temp.append(mult)
                mult = 1
                i+= 1
            elif i == right-1:
                for j in range(left,i):
                    mult *= nums[j]
                temp.append(mult)
                mult = 1
                i+= 1
            else :
                for j in range(left,i):
                    mult *= nums[j]
                for j in range(i+1,right):
                    mult*= nums[j]
                temp.append(mult)
                mult = 1
                i+=1 
        return temp




                
        