

def dfs(root,visited):
    for neighbour in get_neighbours():
        if neighbour in visited:
            continue
        visited.add(neighbour)
        dfs(neighbour,visited=visited)
        
def get_neighbours(node):
    pass