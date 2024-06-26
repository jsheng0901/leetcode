class Node:  # 字符节点
    def __init__(self):  # 初始化字符节点
        self.children = {}  # 初始化子节点
        self.is_end = False  # is_end 用于标记单词结束


class Trie:
    # 字典树
    # 初始化字典树
    def __init__(self):  # 初始化字典树
        self.root = Node()  # 初始化根节点（根节点不保存字符）

    # 向字典树中插入一个单词
    def insert(self, word: str) -> None:
        """
        Time O(n)
        Space O(n)
        遍历整个word
        """
        cur = self.root
        for ch in word:  # 遍历单词中的字符
            if ch not in cur.children:  # 如果当前节点的子节点中，不存在键为 ch 的节点
                cur.children[ch] = Node()  # 建立一个节点，并将其保存到当前节点的子节点
            cur = cur.children[ch]  # 令当前节点指向新建立的节点，继续处理下一个字符
        cur.is_end = True  # 单词处理完成时，将当前节点标记为单词结束

    # 查找字典树中是否存在一个单词
    def search(self, word: str) -> bool:
        """
        Time O(n)
        Space O(1)
        遍历整个word
        """
        cur = self.root
        for ch in word:  # 遍历单词中的字符
            if ch not in cur.children:  # 如果当前节点的子节点中，不存在键为 ch 的节点
                return False  # 直接返回 False
            cur = cur.children[ch]  # 令当前节点指向新建立的节点，然后继续查找下一个字符

        return cur is not None and cur.is_end  # 判断当前节点是否为空，并且是否有单词结束标记

    # 查找字典树中是否存在一个前缀
    def starts_with(self, prefix: str) -> bool:
        """
        Time O(n)
        Space O(1)
        遍历prefix这个word
        """
        cur = self.root
        for ch in prefix:  # 遍历前缀中的字符
            if ch not in cur.children:  # 如果当前节点的子节点中，不存在键为 ch 的节点
                return False  # 直接返回 False
            cur = cur.children[ch]  # 令当前节点指向新建立的节点，然后继续查找下一个字符
        return cur is not None  # 判断当前节点是否为空，不为空则查找成功


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.starts_with("app"))
trie.insert("app")
print(trie.search("app"))
