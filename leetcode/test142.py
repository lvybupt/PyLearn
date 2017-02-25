class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle( head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None or head.next == None :
        return None

    slow_index = fast_index = head

    while fast_index != None and fast_index.next != None :
        fast_index = fast_index.next.next
        slow_index = slow_index.next
        if fast_index == slow_index:
            break
    if fast_index == None or fast_index.next == None :
        return None

    print(slow_index.val)
    print(fast_index.val)
    slow_index = head
    while fast_index != slow_index:
        slow_index = slow_index.next
        fast_index = fast_index.next

    return slow_index

def main():
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)
    a.next = b
    b.next = c
    c.next = d
    d.next = b
    print(detectCycle(a).val)


if __name__ == '__main__':
    main()