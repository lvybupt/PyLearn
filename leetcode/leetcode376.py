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
        fast = nums[1]
        slow = nums[0]
        test = fast-slow
        #subseq.append(slow)
        result = result + 1
        i = 1
        while test == 0 and i < len_nums:
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








