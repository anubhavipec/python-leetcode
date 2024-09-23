class PrefixTree:
    
    def __init__(self) -> None:
        self.children = {}
        self.end = False
        
    def insert(self,word:str) -> None:
        node = self
        
        for char in word:
            if char not in node.children:
                node.children[char] = PrefixTree()
            node = node.children[char]
        node.end = True
    
    def search(self,word:str) -> bool:
        node = self
        
        for char in word:
            if char not in node.children:
                return False
            
            node = node.children[char]
        return node.end
    
    def starts_with(self,word:str) -> bool:
        node = self
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True