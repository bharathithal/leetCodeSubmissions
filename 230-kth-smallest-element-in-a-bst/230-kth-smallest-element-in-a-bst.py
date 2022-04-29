# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = [] 
        self.getAllNums(root, arr)
        return arr[k-1]
        
        
        
    def getAllNums(self, root, arr):
        if not root:
            return
        
        self.getAllNums(root.left, arr)
        arr.append(root.val)
        self.getAllNums(root.right, arr)