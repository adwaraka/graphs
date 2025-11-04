class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.end = False

class TrieBuilder:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str):
        current = self.root
        for alphabet in word:
            if alphabet not in current.nodes:
                current.nodes[alphabet] = TrieNode()
            current = current.nodes[alphabet]
        current.end = True

    def search(self, word: str):
        current = self.root
        for alphabet in word:
            print(current.nodes, len(current.nodes))
            if alphabet not in current.nodes:
                return False
            current = current.nodes[alphabet]
        return current.end

    def startsWith(self, prefix: str):
        current = self.root
        for alphabet in prefix:
            print(current.nodes, len(current.nodes))
            if alphabet not in current.nodes:
                return False
            current = current.nodes[alphabet]
        return True


trie = TrieBuilder()

trie.insert("apple")
trie.insert("applesauce")
trie.insert("applegate")
trie.insert("appleinc")
trie.insert("batman")

print(trie.search("apple"))
print(trie.startsWith("applesauce"))
print(trie.search("applegate"))
print(trie.search("applesauce"))
print(trie.startsWith("bat"))