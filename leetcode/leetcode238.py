class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ##任何一个值都可以看成左右两边的积的积
        if nums ==[]:
        	return []
        len_nums = len(nums)
        tem_n = 1
        result = [[1] for i in range(len_nums)] 

        result[0] = 1
        len_nums = len(nums)
        tem_n = 1
        if len_nums == 1 :
        	return []
        for i in range(0,len_nums-1):  #从左向右
        	result[i+1] = result[i] * nums[i]

        for i in range(len_nums-1,0,-1): #从右向左
        	tem_n = tem_n * nums[i] 
        	result[i-1] = result[i-1] * tem_n

        return result

def main():
	a = [9,0,-2]
	m = Solution()
	print(m.productExceptSelf(a))

if __name__ == '__main__':
	main()