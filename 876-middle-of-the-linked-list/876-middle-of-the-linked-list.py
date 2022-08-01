# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        length = 0
        while curr:
            length +=1
            curr = curr.next
      
        middle = (length // 2) + 1
        
        curr = head
        count = 1
        while count != middle:
            curr = curr.next
            count += 1
        return curr
            
