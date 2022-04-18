# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            nxt = curr.next.next
            sec = curr.next
            
            sec.next = curr
            curr.next = nxt
            prev.next = sec
            
            prev = curr
            curr = nxt
            
        return dummy.next
        