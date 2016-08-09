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
        if(l1 is None and l2 is None):
            return None
        elif(l1 is None):
            return l2
        elif(l2 is None):
            return l1
        if(l1.val <= l2.val):
            fl = l1
            sl = l2
        else:
            fl = l2
            sl = l1
        start = fl
        while(True):
            if(fl.next and sl is not None):
                if(fl.next.val > sl.val):
                    temp = fl.next
                    fl.next = sl
                    if(sl):
                        sl = sl.next
                        fl.next.next = temp
                    else:
                        break
                else:
                    fl = fl.next
            elif(sl):
                fl.next = sl
                break
            else:
                break
        return start
                    
            
            
        