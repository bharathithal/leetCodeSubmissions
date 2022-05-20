# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []
        
        def traverse(node):
            if not node:
                return None
            
            nums.append(node.val)
            traverse(node.left)
            traverse(node.right)
            
        traverse(root)
        nums.sort()
        left, right = 0, len(nums) - 1 
        
        while left < right:
            if nums[left] + nums[right] == k:
                return True
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        
        return False
        