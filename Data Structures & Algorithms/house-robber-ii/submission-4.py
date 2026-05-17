class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 2:
            return max(nums)
        def houserob(houses):
            if len(houses) == 1 or len(houses) == 2 :
                return max(houses)
            dp = [0]*(len(houses)+1)
            dp[0] = houses[0]
            dp[1] = max(houses[0],houses[1])
            for i in range(2,len(houses)):
                dp[i] = max(dp[i-1],dp[i-2]+houses[i])
            return max(dp)
        max1 = houserob(nums[:-1])
        max2 = houserob(nums[1:])
        return max(max1,max2)

        
        