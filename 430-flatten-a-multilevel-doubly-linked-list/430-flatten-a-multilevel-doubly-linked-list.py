"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        nodes = []
        def dfs(node):
            if node is None:
                return
            nodes.append(node)
            if node.child:
                dfs(node.child)
            if node.next:
                dfs(node.next)
            
        dfs(head)
        head = nodes[0]
        head.child = None
        
        for i in range(1, len(nodes)):
            node = nodes[i]
            prev = nodes[i-1]
            node.child = None
            node.prev = prev
            prev.next = node
        
        return head
            