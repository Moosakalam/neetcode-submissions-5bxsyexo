class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_enco = 0

        for i in range(len(prices) - 1):
            x = prices[i]

            for j in range(i + 1, len(prices)):
                if prices[j] - x > max_enco:
                    max_enco = prices[j] - x

        return max_enco
                

        
        