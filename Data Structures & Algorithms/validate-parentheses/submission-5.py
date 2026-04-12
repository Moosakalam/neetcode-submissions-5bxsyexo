class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        if len(s) == 0 :
            return False 
        if len(s) == 1 :
            return False
        for i in s:
            print(a)
            
            if i == ']':
                if not a:
                    return False 
                x = a.pop()
                if x!= '[':
                    return False
            
            elif i == '}':
                if not a:
                    return False
                x = a.pop()
                if x!= '{':
                    return False


            elif i == ')':
                if not a:
                    return False
                x = a.pop()
                if x!= '(':
                    return False
            
            else:
                a.append(i)
        if len(a) > 0 :
            return False
        return True
        