# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin = list()
        temp = head
        num = 0
        pow = 1
        
        while temp != None:
            bin.append(temp.val)
            temp = temp.next
            
        bin.reverse()
        
        for digit in bin:
            num = num + digit * pow
            pow = pow * 2
        
        return num
        