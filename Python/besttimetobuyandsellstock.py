class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return
        max = prices[len(prices)-1]
        profit = 0 
        
        for item in prices[::-1]:
            if max -item > profit:
                profit = max -item 
            if item > max:
                max= item
        return profit        
            
        
        
