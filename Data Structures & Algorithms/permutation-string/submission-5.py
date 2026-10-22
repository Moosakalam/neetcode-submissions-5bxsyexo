class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:  
      
         
        s1 = list(s1)
        s2 = list(s2)
        l =len(s1)
        output = False
        for i in range(0,len(s2)):
            if sorted(s1) == sorted(s2[i:i+l]):
                return True 
        return False

            
        