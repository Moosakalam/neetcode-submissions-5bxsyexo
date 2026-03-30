class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        retur = []
        temp = []
        for i in range(len(strs)):
            if strs[i] == ",":
                continue
            z = sorted(list(strs[i]))
            
            temp.append(strs[i])
            for j in range(i+1,len(strs)):
                
                k =  sorted(list(strs[j]))
                
                if z == k :
                    temp.append(strs[j])
                    strs[j] = ","
                    print(temp)
            retur.append(temp)
            temp = []
        return retur




        