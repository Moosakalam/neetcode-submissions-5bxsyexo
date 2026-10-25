class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        res = [0]*len(temperatures)
        for i,e in enumerate(temperatures):
            while stack and e > stack[-1][0]:
                stace , stacki = stack.pop()
                res[stacki] = i - stacki
            stack.append([e,i])
        return res 

        

        