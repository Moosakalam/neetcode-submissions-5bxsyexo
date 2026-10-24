class MinStack:

    def __init__ (self):
        self.items = []
    def push(self ,val) -> void:
        self.items.append(val)
    def pop(self) ->int:
        return self.items.pop()
    def top(self) -> int :
        return self.items[-1]
    def getMin(self) -> int:
        return min(self.items)
        
