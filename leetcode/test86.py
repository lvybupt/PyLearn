class ListNode(object):
        def __init__(self, x):
                self.val = x
                self.next = None




def partition( head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        
        """
        if head == None or head.next == None:
        	return head

        result = head

        bfirst = None
        slast = None
        storage = None

        while head != None:
                print(head.val)
        	if head.val <x :
        		if bfirst == None :
        			slast = head
        			storage = head
                                print('111')
                                print(head)
                                print(slast)
                                #print(slast.val)
        		else :
        			storage.next = head.next
        			if slast == None :
        				result = head
        			else :
        				slast.next = head 
        			slast = head
                                print(slast.val)
        			slast.next = bfirst
        	else :
        		if bfirst == None :
        			bfirst = head
        		storage = head

        	
        	head = storage.next
        return result

def main():
        a = ListNode(1)
        b = ListNode(3)
        c = ListNode(2)
        a.next = b
        b.next = c
        z = partition(a,3)
        print(z.val,z.next.val,z.next.next.val)

if __name__ == '__main__':
        main()