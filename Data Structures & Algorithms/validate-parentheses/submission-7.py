class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        stack = deque()
          
        for i in s:
            if i in '({[':
                stack.append(i)
                
            else:
                if not stack:
                    return False 
            
                lastele = stack.pop()

                if (lastele == '[' and i != ']') or (lastele == "{" and i != "}") or (lastele == "(" and i != ")"):
                    return False 
                
        return len(stack) == 0  
        
        