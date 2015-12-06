
"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")

"""


class TrieNode(object):
    def __init__(self):
        self.isWord = False
        self.d = {}


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for s in word:
            if s not in node.d:
                node.d[s] = TrieNode()
            node = node.d[s]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.match(self.root, 0, word)

    def match(self, node, index, word):

        if index == len(word):
            return node.isWord

        char = word[index]

        if char == '.':

            for ss in node.d:
                if self.match(node.d[ss], index + 1, word):
                    return True
            return False

        else:
            return char in node.d and self.match(node.d[char], index + 1, word)

if __name__ == '__main__':
    wd = WordDictionary()

    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print(wd.search('bad'))
    print(wd.search('ba'))
    print(wd.search('ba.'))

    print(wd.search("pad"))   # -> false
    print(wd.search("bad"))   # -> true
    print(wd.search(".ad"))   # -> true
    print(wd.search("b.."))   # -> true

