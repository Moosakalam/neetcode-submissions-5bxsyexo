class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices :
            return 0 
        l , r = 0 , 1
        max_profit = 0 
        profit = 0 
        for i in range(len(prices)-1):
            buying = prices[i]
            for j in range(i+1,len(prices)):
                selling = prices[j]
                profit = selling-buying
                if max_profit<profit:
                    max_profit=profit
        return max_profit



        