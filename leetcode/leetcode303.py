class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1])
        
#######优先家里预处理的计算增加函数效率      
class NumArray(object):
    def __init__(self, nums):
        self.dp = nums
        for i in xrange(1, len(nums)):
            self.dp[i] += self.dp[i-1]

    def sumRange(self, i, j):
        return self.dp[j] - (self.dp[i-1] if i > 0 else 0)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)