class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l1 = []
        dict1 = dict()
        for i in nums:
            if i in dict1:
                dict1[i] += 1 
            else :
                dict1[i] = 1 
        
        for j in range(k):
            max_1 = max(dict1.values())
            for key , value in dict1.items():
                if value == max_1:
                    l1.append(key)
                    del dict1[key]
                    break

            

        return l1

        