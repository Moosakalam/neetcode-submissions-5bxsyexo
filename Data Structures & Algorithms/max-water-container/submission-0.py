class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_max = 0 
        current_water = 0 
        i = 0
        j = i+1
        while i <= len(heights) - 2:
            heig = min(heights[i],heights[j])
            current_water = heig * (j-i)
            if current_water > current_max:
                current_max = current_water
                current_water = 0
                if j == len(heights)-1:
                    i+=1 
                    j=i+1
                else:
                    j+=1 

            elif j == len(heights)-1:
                i += 1
                j = i+1
            else:
                j+=1   
        return current_max
        