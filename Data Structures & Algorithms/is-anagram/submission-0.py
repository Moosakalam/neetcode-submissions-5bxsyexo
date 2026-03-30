class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a1 = sorted(list(s))
        a2 = sorted(list(t))
        if a1 == a2:
            return True
        else:
            return False

        