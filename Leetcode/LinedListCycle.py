# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if(head == None):
            return False 
        if(head.next == None):
            return False
        first = head
        if(head.next):
            second = head.next
        else:
            return False
        while(True):
            if(first == second):
                return True
            if(second.next and second.next.next):
                second = second.next.next
                first = first.next 
            else:
                break
        return False
        
            