# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 1
        temp = head
        
        while temp.next:
            length += 1
            temp = temp.next
            
        if(length == 1):
            head = None
            
        elif(length == n):
            temp = head
            head = head.next
            temp.next = None
            
        else: 
            temp, prev = head, None
    
            for i in range(length-n):
                prev = temp
                temp =  temp.next
        
            prev.next = temp.next
        
        return head
        