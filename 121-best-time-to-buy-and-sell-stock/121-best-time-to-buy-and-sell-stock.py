class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        
        max_profit = 0      
        purchase = prices[0] 
        for price in prices:
            
            profit = price - purchase
            if profit > max_profit:
                max_profit = profit
            if price < purchase:
                purchase = price
        if max_profit > 0:               
            return max_profit
        return 0
    

                    
            
                    