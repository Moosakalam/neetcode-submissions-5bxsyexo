class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:  
        l = 0 
         
        s1 = list(s1)
        s2 = list(s2)
        output = False

        for i in range(len(s1),len(s2)+1):
            
            if sorted(s1) == sorted(s2[l:i]):
                output = True
                l+=1
            else:
                l+=1
                
        return output 

            
        