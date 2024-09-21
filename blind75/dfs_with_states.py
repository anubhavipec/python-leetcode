
#Given a ternary tree (each node of the tree can have up to three children), 
# find all the root-to-leaf paths.

def ternary_root_paths(root):
    
    #dfs helper function
    def dfs(root,path,res):
        
        if all(c is None for c in root.childeren):
            res.append('->'.join(path) + '->'+str(root.val))
            return
        
        #dfs on each non null child
        
        for child in root.children:
            if child is not None:
                path.append(str(root.val))
                dfs(child,path,res)
                path.pop()
    res = []
    if root:dfs(root,[],res)
    return res


path = [1,2,3]
print(path+[5,6])