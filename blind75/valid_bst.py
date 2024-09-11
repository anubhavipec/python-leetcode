class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node:Optional[TreeNode],left,right):
            if not node:
                return True
            
            if not (node.val < right and node.val> left):
                return False
            
            return isValid(node.left,left,node.val) and isValid(node.right, node.val,right)
        
        return isValid(root,float("-inf"),float("inf"))