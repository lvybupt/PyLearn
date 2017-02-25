
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    @param head: The first node of the linked list.
    @return: the node where the cycle begins. 
                If there is no cycle, return null
    """
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None :
            return None
        slow_index = fast_index = head 
        ### fast 以两倍速度跑，相遇，然后slow回head，以相同速度 跑，相遇点为结果点

        while fast_index != None and fast_index.next != None :
            fast_index = fast_index.next.next
            slow_index = slow_index.next
            if fast_index == slow_index:
                break
        if fast_index == None or fast_index.next == None :
            return None

        slow_index = head

        while fast_index != slow_index:
            slow_index = slow_index.next
            fast_index = fast_index

        return slow_index

