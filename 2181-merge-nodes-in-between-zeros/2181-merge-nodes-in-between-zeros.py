# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp  = head.next
        dummy = ListNode(0, None)
        tail = dummy
        
        while temp != None:
            sum = 0
            while temp.val != 0:
                sum += temp.val
                temp = temp.next
            
            node = ListNode(sum, None)
            tail.next = node
            tail = tail.next
            temp = temp.next
            
        return dummy.next
            