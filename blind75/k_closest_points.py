from heapq import heappop, heappush
from typing import List, Tuple

def k_closest_points(points: List[List[int]],k:int) -> List[List[int]]:
    # by default first element of the tuple will
    # be used to decide position in heap
    heap: List[Tuple[int,List[int]]] = []
    
    
    for pt in points:
        heappush(heap,(pt[0] ** 2 + pt[1]**2,pt))
    res = []
    
    for _ in range(k):
        _,pt = heappop(heap)
        res.append(pt)
    return res