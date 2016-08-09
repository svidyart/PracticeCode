# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if(not headA or not headB):
            return None
        if(headA is headB):
            return headA
        d = set()
        d.add(headA)
        while(True):
            if(headA.next):
                d.add(headA.next)
                headA = headA.next
            else:
                break
        if(headB in d):
            return headB
        while(True):
            if(headB.next):
                if(headB.next in d):
                    return headB.next
                d.add(headB.next)
                headB = headB.next
            else:
                return None