class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        h = len(nums)-1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        while l<h:
            mid = int((l+h)/2)
            print(mid)
            if target == nums[mid]:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else:
                h = mid
        if nums[-1] == target:
            return len(nums)-1
        else:
            return -1 

        