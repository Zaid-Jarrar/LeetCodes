# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        if not head:
            return None
        intersect = getIntersect(head)
        if not intersect:
            return None
        
        tortoise  = head
        hare = intersect
        while hare != tortoise:
            tortoise = tortoise.next
            hare = hare.next
        return hare
    
       
    
def getIntersect(head):
    
    # slow = head
    # fast = head
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
            
        if fast == slow:          
            return fast         
      
    return None
    
    
            
        