


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack(i, x):
           
            if x == 0:
                res.append(sol[:])
                return
            
            if i == n:
                return

            backtrack(i + 1, x)

            if nums[i] <= x:
                sol.append(nums[i])
                
                backtrack(i, x - nums[i])
      
                sol.pop()

        backtrack(0, target)
        return res
        