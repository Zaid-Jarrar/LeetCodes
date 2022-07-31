# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # base case for the recursion to stop where it would return the true value of the logical operation 
        # if list 1 is none , and list 2 is not, list2 will be returned
        if not list1 or not list2:
            return list1 or list2
        
        # if value of listNode1 is smaller than  value of listNode2
        elif list1.val < list2.val:
            
            # connect the listNode1 next pointer to the recursive call of ListNode1.next and ListNode2
            list1.next = self.mergeTwoLists(list1.next,list2)
            
            # return the ListNode1 
            return list1
        
        # if value of listNode1 is bigger or equal than value of listNode2
        else:
            # connect the listNode2 next pointer to the recursive call of ListNode1 and ListNode2.next
            list2.next = self.mergeTwoLists(list1,list2.next)
            
            # return the ListNode2 
            return list2
            
