class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None:
            return 0
        
        max_profit = 0      
        purchase = prices[0]
        
        for price in prices:      
            profit = price - purchase
            if profit > max_profit:
                max_profit = profit
            if price < purchase:
                purchase = price    
                     
        return max_profit
        
        
    

                    
            
                    