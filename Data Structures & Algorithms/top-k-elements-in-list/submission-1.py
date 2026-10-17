class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = []
        z = []
        for i in nums:
            count[i] = 1 + count.get(i,0) 
        for i , v in count.items():
            arr.append([v,i])
        arr.sort()
        for i in range (k) :
            z.append(arr.pop()[1])
        return z 

        
        