# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i, length = 0, 1
        temp = head
        temp1 = head
        
        while temp != None:
            length += 1
            temp = temp.next
        
        while i != (k-1):
            temp1 = temp1.next
            i += 1
        
        i = 0
        temp2 = head
        
        while i != (length-k-1):
            temp2 = temp2.next
            i += 1
            
        temp1.val, temp2.val = temp2.val, temp1.val
        
        return head
        