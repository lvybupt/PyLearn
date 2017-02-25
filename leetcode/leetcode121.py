class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        len_index = len(prices)
        little = prices[0]
        value = 0
        for i in range(0,len_index) :
        	if prices[i] <= little :
        		little = prices
        	elif (prices[i] - little) > value :
        		value = prices[i] - little

        return value
