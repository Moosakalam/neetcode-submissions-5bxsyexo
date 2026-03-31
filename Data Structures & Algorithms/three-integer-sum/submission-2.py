class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        retur = []
        nums = sorted(nums)
        left = 0 
        right = len(nums)-1
        for i in range(len(nums)):
            k =len(nums)-1
            j = i+1
            while j<k:
                sum = nums[i]+ nums[j]+nums[k]
                if sum == 0 :
                    a = [nums[i],nums[j],nums[k]]
                    if a not   in  retur:
                        retur.append([nums[i],nums[j],nums[k]])
                if sum > 0 :
                    k-=1
                else:
                    j+=1
                
        return  retur

        