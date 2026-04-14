class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top , bottom = 0 , len(matrix) - 1
        while top<=bottom:
            row = (top+bottom)//2
            if target> matrix[row][-1]:
                top = row+1
            elif target<matrix[row][0]:
                bottom = row-1
            else:
                break
        nums = matrix[row]
        mid = (0 + len(nums)-1)//2
        l = 0 
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return True
            elif target> nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return False

        
        