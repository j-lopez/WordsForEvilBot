
class TrieNode:

    def __init__(self):
        self.value = None
        self.children = [None] * 26
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def insert(self, word):

        n = len(word)
        currNode = self.root

        for i in range(n):
            letter = ord(word[i]) - ord('A')

            if not currNode.children[letter]:
                currNode.children[letter] = TrieNode()
                currNode.children[letter].value = chr(letter + ord('A'))

            currNode = currNode.children[letter]

        currNode.endOfWord = True

    def search(self, word):

        if (word != word.upper()):
            return False

        n = len(word)
        currNode = self.root

        for i in range(n):
            letter = ord(word[i]) - ord('A')
            if not currNode.children[letter]:
                return False

            currNode = currNode.children[letter]

        if not currNode.endOfWord:
            return False

        return True

    def getChildren(self, path):

        if path != path.upper():
            return []

        n = len(path)
        currNode = self.root

        for i in range(n):
            letter = ord(path[i]) - ord('A')

            if not currNode.children[letter]:
                return []

            currNode = currNode.children[letter]
        if sum([0 if currNode.children[i] else 1 for i in range(26)]) > 0:
            return currNode.children
        else:
            return None






