from collections import deque

import sys
from typing import Dict,List

def task_scheduling(tasks: List[str],requirements:List[List[str]]) -> List[str]:
    
    graph: Dict[str,List[str]] = {t: {} for t in tasks}
    
    for a,b in requirements:
        graph[a].append(b)
    return topo_sort(graph)


def find_indegree(graph):
    
    indegree = {node:0 for node in graph}
    
    for node in graph:
        for neighbour in graph[node]:
            indegree[neighbour] += 1
    return indegree




def topo_sort(graph):
    
    res = []
    
    indegeree = find_indegree(graph=graph)
    q = deque()
    for nodes in indegeree:
        q.append(nodes)
    while len(q) > 0:
        node = q.popleft()
        res.append(node)
        for neighbours in graph[node]:
            indegeree[neighbours] -= 1
            if indegeree[neighbours] == 0:
                q.append(neighbours)
    return res if len(graph) == len(res) else None
    

