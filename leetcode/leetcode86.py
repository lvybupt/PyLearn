# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        
        """
        if head == None or head.next == None:
        	return head

        result = head

        bfirst = slast = storage = None

        while head != None:
        	if head.val <x :
        		if bfirst == None :
        			slast = storage = head
        		else :
        			storage.next = head.next
        			if slast == None :
        				result = head
        			else :
        				slast.next = head 
        			slast, slast.next = head, bfirst
        	else :
        		if bfirst == None :
        			bfirst = head
        		storage = head

        	
        	head = storage.next
        return result
        		



        '''
        a = head 
        if head = None or head.next = None:
        	return head



        q = head.next
        index2 = q 
        head = q
        while head.next != None:
        	if head.next.val < x:
        		index2.next = head.next
        		index2 = head.next
        		head.next = head.next.next
        	else :
        		head = head.next

        if a.val < x and q.val < x:
        	index2.next = a.next 
        	a.next = q
        elif a.val < x and q.val >= x :
        	index2.next,a.next,q.next = q,q.next,a.next
        	#a.next = q.next 
        	#q.next = a.next
        elif a.val >=x and q.val >= x :
        	a ,index2.next  = q.next , a
        	index2.next.next ,index2.next.next.next = q , index2.next.next
        elif a.val >=x and q.val <x :
        	a , index2.next = q , a

        return a

        '''




        '''
        result = head
        re_1 = ListNode(123)
        re_2 = ListNode(321)

        index1 = re_1
        index2 = re_2

        while head != None :
        	if head.val < x :
        		index1.next  = head 
        		index1 = head 
        		head = head.next
        	else :
        		index2.next = head
        		index2 = head
        		head = head.next

        if re_1.next == None or re_2.next == None :
        	return result
        else :
        	result = re_1.next 
        	index1.next = re_2.next
        	return result
        '''

        