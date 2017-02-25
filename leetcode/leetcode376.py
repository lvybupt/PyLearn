class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        len_nums = len(nums)

        if len_nums == 0 :
        	return result
        elif len_nums ==1 :
            return 1

        #subseq = []
        fast = nums[1] # 目前发现的最合适的拐点，作为拐点的备选点
        slow = nums[0] # 确定的拐点
        test = fast-slow # 记录是向上还是向下
        #subseq.append(slow)
        result = result + 1
        i = 1 # 遍历的变量
        while test == 0 and i < len_nums:
            ##去掉数列开始时没用波动的部分
        	fast = nums[i]
        	test = fast - slow
        	i = i+1
        if test == 0 :
        	return 1

        #subseq.append(fast)
        result = result + 1

        while i < len_nums:
        	#fast = nums[i]
        	#test = fast-slow
        	if (nums[i] - fast)*test < 0:
        		slow = fast 
        		fast = nums[i]
        		#slow = nums[i]
        		#subseq.append(slow)
        		result = result + 1
        	elif (nums[i] - slow) * (nums[i] - slow) > test * test:
        		fast = nums[i]

        	test = fast - slow 
        	i = i+1
        return result








