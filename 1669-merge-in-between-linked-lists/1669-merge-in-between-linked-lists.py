# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp1, temp2 = list1, list1
        anode, bnode = None, None
        
        i = 0
        while i != (a-1):
            temp1 = temp1.next
            i += 1
        anode = temp1
        
        i = 0
        while i != b+1:
            temp2 = temp2.next
            i += 1
        bnode = temp2
        
        temp = list2
        while temp.next != None:
            temp = temp.next
        
        temp.next = bnode
        anode.next = list2
        
        return list1
            