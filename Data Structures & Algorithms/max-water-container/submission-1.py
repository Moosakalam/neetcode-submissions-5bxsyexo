class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0 
        l = len(heights)-1
        width = 0 
        height = 0 
        maxarea = 0 
        while i < l :
            
            area = (l-i) * min(heights[i],heights[l])
            if maxarea < area:
                maxarea = area 
            if heights[i] < heights[l]:
                i+=1
            else:
                l-=1
        return maxarea
            


            


        