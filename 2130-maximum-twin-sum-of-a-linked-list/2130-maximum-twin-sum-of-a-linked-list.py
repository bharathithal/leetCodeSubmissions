# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        second = None
        
        while fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        slow.next = None
        prev, curr = None, second
        
        while (curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        temp1, temp2 = head, prev
        res = 0
        while(temp1 != None and temp2 != None):
            sum = temp1.val + temp2.val
            res = max(sum, res)
            temp1 = temp1.next
            temp2 = temp2.next
            
        return res
            
            