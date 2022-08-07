class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # max=0
        # difference =0
        # for index in range(len(prices)):
        #     sell=0
        #     #min of list is the buy and max of the sell and caluctate the diff
        #     # buy = prices[index]
        #     for price in range((index+1),len(prices)):
        #         if prices[price] > buy and prices[price] > sell:
        #             sell = prices[price]
        #             difference = sell - buy
        #     if difference > max:
        #         max = difference
        # if max > 0:
        #     return max
        # return 0
        
        
        # difference = 0
        # max_profit = 0
        # for index in range(len(prices)):
        #     sell=0
        #     buy = prices[index]
        #     sell_list = prices[index+1:]
        #     if sell_list:
        #         sell = max(sell_list)
        #     if sell > buy:
        #         difference = sell - buy
        #         if difference > max_profit:
        #             max_profit  = difference
        # if max_profit>0:
        #     return max_profit
        # return 0
        
        maxProfit = 0      
        miniBuy = prices[0] 
        for price in prices:
            
            profit = price - miniBuy
            if profit > maxProfit:
                maxProfit = profit
            if price < miniBuy:
                miniBuy = price
        if maxProfit > 0:               
            return maxProfit
        return 0
                    
            
                    
            
#        2-5 2-7 2-10
#         3   5   8
        
#         7-10
#          3  