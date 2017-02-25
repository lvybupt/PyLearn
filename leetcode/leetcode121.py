class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        len_index = len(prices)
        little = prices[0] # 记录发现的最小点
        value = 0 # 记录最大价值
        for i in range(0,len_index) :
        	if prices[i] <= little :
        		little = prices
        	elif (prices[i] - little) > value :
        		value = prices[i] - little

        return value
