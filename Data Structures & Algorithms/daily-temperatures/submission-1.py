class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = []
        i = 0 
        j = 0
        if len(temperatures) == 1:
            return [0]
        while i<len(temperatures):
            if j<len(temperatures):
                if temperatures[i] >= temperatures[j]:
                    j+=1
                else:
                    ret.append(j-i)
                    i+=1
                    j=i+1
            else:
                ret.append(0)
                i+=1
                j=i+1
        return ret
        

            


        