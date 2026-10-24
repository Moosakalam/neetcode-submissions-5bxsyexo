class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque 
        stack = deque()
        for i in tokens :
            if i not in "+-/*" :
                stack.append(i)
            else:
                firnum = int(stack.pop())
                secum = int(stack.pop())
                
                if i == '+' :
                    fi = secum + firnum 
                elif i == '-':
                    fi = secum - firnum 
                elif i == "*":
                    fi = secum * firnum 
                else:
                    fi = int(secum / firnum) 
                stack.append(fi)
                
        return(int(stack.pop()))


