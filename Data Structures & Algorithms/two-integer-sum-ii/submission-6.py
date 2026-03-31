class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        j = len(numbers)-1 
        
        while i < j :
            sum1 = numbers[i] + numbers[j]
            if sum1 == target:
                return [i+1,j+1]
            elif j == i+1:
                i+=1 
                j = len(numbers)-1
            else:
                j-=1
        
        
        
            

            
             
            


        