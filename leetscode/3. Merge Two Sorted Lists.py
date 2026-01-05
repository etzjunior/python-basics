# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = curr = ListNode()  # One line setup
        
        while list1 or list2:      # Single condition
            if list1 and (not list2 or list1.val <= list2.val):
                curr.next = list1; list1 = list1.next
            else:
                curr.next = list2; list2 = list2.next
            curr = curr.next
        
        return dummy.next
