# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head,prev=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return prev
        
        
        nex = head.next
        head.next = prev
        prev = head
        head = nex

        return self.reverseList(head,prev)
        