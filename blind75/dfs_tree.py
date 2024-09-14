def dfs(root,target):
    if not root:
        return None
    
    if root.val == target:
        return root
    
    left = dfs(root.left,target=target)
    if left is not None:
        return left
    return dfs(root=root.right,target=target)