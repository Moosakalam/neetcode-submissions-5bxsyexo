class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0 
        pl = len(numbers) - 1 
        z = 0 
        while p1 < pl:
            z = numbers[p1]+numbers[pl]
            if z == target:
                return [p1+1,pl+1]
            if z > target:
                pl -= 1 
            else:
                p1+=1 
        

        
        
        
            

            
             
            


        