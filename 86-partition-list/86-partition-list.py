# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyL = ListNode(0, None)
        dummyR = ListNode(0, None)
        tail1, tail2 = dummyL, dummyR
        temp = head
        
        while temp:
            if temp.val < x:
                tail1.next = temp
                tail1 = tail1.next
            else:
                tail2.next = temp
                tail2 = tail2.next
            temp = temp.next
        
        tail2.next = None
        tail1.next = dummyR.next
        
        return dummyL.next