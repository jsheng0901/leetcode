from collections import defaultdict


class WordDictionary1:
    """hash map method"""
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length_to_word = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.length_to_word[len(word)].add(word)

    def search(self, word: str) -> bool:
        if word in self.length_to_word[len(word)]:
            return True
        else:
            for w in self.length_to_word[len(word)]:
                match_num = 0
                for i in range(len(w)):
                    if w[i] == word[i] or word[i] == '.':
                        match_num += 1
                if match_num == len(w):
                    return True

            return False


class WordDictionary2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie

        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True

    def search(self, word: str) -> bool:
        """
        O(m) with no '.', O(N * 26 ^ M) worse case
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any letter
        trie structure, nested dictionary, ex: 'dog' -- {'d': {'o': {'g': {'$': True} } } } go through each layer
        finally find $ in last layer dictionary then means this word in trie
        """

        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == '.':
                        for x in node:
                            if x != '$' and search_in_node(word[i + 1:], node[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return '$' in node

        return search_in_node(word, self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)