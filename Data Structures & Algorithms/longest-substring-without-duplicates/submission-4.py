class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0 
        count = 0
        l , r = 0,0
        stri = set()  
        for r in range(len(s)):
            while s[r] in stri:
                stri.remove(s[l])
                l+=1
                print('inner')
                print(stri)

            stri.add(s[r])
            print(stri)
            count = r-l+1
            max_count = max(max_count,count)
        max_count = max(max_count,count)
        return max_count
            

        

       

            
        