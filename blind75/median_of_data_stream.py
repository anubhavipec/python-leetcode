from heapq import heappop,heappush

class MedianOfStream:
    
    def __init__(self):
        self.max_heap = [] # this will hold smaller pile of numbers
        self.min_heap = [] # this will hold larger pile of numbers
        
    def add_number(self,num: float) -> None:
        
        if len(self.min_heap) == 0 or num < self.min_heap[0]:
            heappush(self.max_heap,-num)
            
        else:
            heappush(self.min_heap,num)
            
        self._balance()
        
    def get_medians(self)-> float:
        if len(self.max_heap) == len(self.min_heap) :
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0] 
        
    def _balance(self) -> None:
        
        if len(self.max_heap) < len(self.min_heap):
            val = heappop(self.min_heap)
            heappush(self.max_heap, -val)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = heappop(self.max_heap)
            heappush(self.min_heap,-val)