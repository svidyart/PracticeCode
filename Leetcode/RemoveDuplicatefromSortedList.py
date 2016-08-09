# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None):
            return 
        temp = head
        while(temp.next != None):
            if(temp.next.val == temp.val):
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
                