class NodeList:
    def __init__(self,key=0,value=0):
        self.value = value 
        self.next = None 
        self.prev = None 
        self.key = key 
class LRUCache:


    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        self.head = NodeList()
        self.tail = NodeList()
        self.head.next = self.tail
        self.tail.prev = self.head
    def _remove(self,node:NodeList):
        prev = node.prev
        nxt = node.next 
        prev.next = nxt
        nxt.prev = prev 
    def _add(self,node:NodeList):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        temp.prev = node 
        self.head.next = node  

        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value 
        return -1 
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        new_node = NodeList(key,value)
        self._add(new_node)
        self.cache[key] = new_node
        if len(self.cache) > self.capacity:
            lst_node = self.tail.prev
            self._remove(lst_node)
            del self.cache[lst_node.key]
        
