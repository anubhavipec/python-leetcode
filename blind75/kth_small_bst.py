
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        def inroder( root:Optional[TreeNode],values:List[int]) -> List[int]:
            if root:
                inroder(root=root.left,values=values)
                values.append(root.val)
                inroder(root=root.right,values=values)
            return values
        values = inroder(root=root,values = values)
        return values[k-1]
        
        