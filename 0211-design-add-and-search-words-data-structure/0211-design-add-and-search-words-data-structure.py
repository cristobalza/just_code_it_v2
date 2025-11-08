class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict()
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()

            curr = curr.children[letter]

        curr.is_word = True
        

    def search(self, word: str) -> bool:

        def dfs(root, i):
            node = root

            for j in range(i, len(word)):
                if word[j] == ".":
                    for child in node.children.values():
                        if dfs(child, j + 1):
                            return True
                    return False

                else:
                    if word[j] not in node.children:
                        return False

                    node = node.children[word[j]]
                
            return node.is_word


        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)