class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        for i in nums:
            le = nums.pop()
            if le in nums:
                return True
            
        return False 

        