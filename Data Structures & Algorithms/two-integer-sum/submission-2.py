class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,j in enumerate(nums):
            left = target - j 
            if left in dic:
                return [dic[left],i]
            dic[j] = i 