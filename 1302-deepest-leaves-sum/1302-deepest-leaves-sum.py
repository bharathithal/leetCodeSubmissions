# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        prev_level = []
        traversal_queue = [ root ]
        
        while traversal_queue:
            
            next_level_queue = []
			
            for cur_level_node in traversal_queue:
                
                if cur_level_node.left:
                    next_level_queue.append( cur_level_node.left )    
                
                if cur_level_node.right:
                    next_level_queue.append( cur_level_node.right )
			
            prev_level, traversal_queue = traversal_queue, next_level_queue

        return sum( node.val for node in prev_level if node )