class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = []
        s = s.lower()
        for i in s:
            if i.isalnum():
                j.append(i)
        if j == j[::-1]:
            return True 
        return False

        

        