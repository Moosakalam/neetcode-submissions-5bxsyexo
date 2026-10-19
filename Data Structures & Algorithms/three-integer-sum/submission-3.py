class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        retue = []
        sum1 = 0 
        nums.sort()
        for i in range(len(nums)):
            j = i+1
            k = len(nums) -1 
            while j<k:
                sum1 = nums[i] + nums[j] + nums[k]
                if sum1 == 0 :
                    if [nums[i],nums[j],nums[k]] not in retue:
                        retue.append([nums[i],nums[j],nums[k]])
                if sum1>0:
                    k -=1 
                else:
                    j+=1 
        return retue 

                    


        