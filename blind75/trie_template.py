class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.freq = 0
    
    def insert(self,word):
        node = self
        for char in word:
            # If character is not a child, we need to add it
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
            node.freq += 1
    
    def query(self,prefix):
        node = self
        
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.freq