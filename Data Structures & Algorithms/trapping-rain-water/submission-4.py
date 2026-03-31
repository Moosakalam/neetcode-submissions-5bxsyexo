class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        units = 0

        while left < right:
            # Strategy: Process the side with the shorter "maximum wall"
            if height[left] < height[right]:
                # If current height is less than the max seen on left, it traps water
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    units += left_max - height[left]
                left += 1
            else:
                
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    units += right_max - height[right]
                right -= 1
                
        return units  
                
                
                
                
                 


    