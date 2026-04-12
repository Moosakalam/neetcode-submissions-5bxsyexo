class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = []
        x = 0 
        for i in tokens:
            print(a)
            if i == '+':
                x = a[-1]+a[-2]
                
                a.pop()
                a.pop()
                a.append(x)
            elif i == '*':
                x = a[-1]*a[-2]
                a.pop()
                a.pop()
                a.append(x)
            elif i == '/':
                x = int(a[-2]/a[-1])
                a.pop()
                a.pop()
                a.append(x)
            elif i == '-':
                x = a[-2]-a[-1]
                a.pop()
                a.pop()
                a.append(x)
            else: 
                a.append(int(i))
       
        return a[0]
        