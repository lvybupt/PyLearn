# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1 != None and l2 != None:
            if l1.val < l2.val :
                result,rindex,l1 = l1,l1,l1.next
            else :
                result,rindex,l2 = l2,l2,l2.next

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                rindex.next,rindex,l1 = l1,l1,l1.next
            else :
                rindex.next,rindex,l2 = l2,l2,l2.next

        if l1 == None and l2 != None :
            rindex.next = l2    
        elif l2 == None and l1 != None :
            rindex.next = l1

        return result



        