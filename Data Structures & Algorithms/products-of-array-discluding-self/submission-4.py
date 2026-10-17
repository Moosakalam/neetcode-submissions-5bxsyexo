
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix1 = []
        suf = 1
        prev = 1

        for i in range(len(nums)):
            prefix.append(1)
            suffix1.append(1)

        

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
            else:
                prev *= nums[i - 1]
                prefix[i] = prev

        suf = 1

        for i in range(len(nums) - 1, -1, -1):
            suffix1[i] = suf
            suf *= nums[i]

        res = []

        for i in range(len(nums)):
            if i == 0:
                res.append(suffix1[i])
            elif i == len(nums) - 1:
                res.append(prefix[i])
            else:
                res.append(suffix1[i] * prefix[i])

        return res



