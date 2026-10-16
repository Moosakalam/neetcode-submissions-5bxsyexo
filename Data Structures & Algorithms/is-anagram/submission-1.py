class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        r = sorted(t)
        if s ==r :
            return True 
        return False
        