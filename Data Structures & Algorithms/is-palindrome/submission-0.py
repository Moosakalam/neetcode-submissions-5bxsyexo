class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s)-1 
        s = s.lower()
        
        while i <= j :
            if s[j].isalnum() and s[i].isalnum():
                if s[i] == s[j]:
                    i+=1
                    j-=1 
                else:
                    return False 
            elif s[j].isalnum() == False:
                j-=1
            else:
                i+=1 
        return True 

        

        