from heapq import heappush,heappop
from typing import List,Tuple

def merge_k_sorted_list(lists: List[List[int]]) -> List[int]:
    
    res:List[int] = []
    
    heap:List[Tuple[int,List[int],int]] = []
    for internal_list in lists:
        heappush(heap,(internal_list[0],internal_list,0))
    
    while heap:
        val,current_list,heap_index = heappop()
        
        res.append(val)
        heap_index += 1
        
        if heap_index <= len(current_list):
            heappush(heap,(current_list[heap_index],current_list,heap_index))
    return res