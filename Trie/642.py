from typing import List
import heapq


class Node:  # 字符节点
    def __init__(self):  # 初始化字符节点
        self.children = {}  # 初始化子节点
        self.is_end = False  # is_end 用于标记单词结束
        self.word = ""      # 记录最终是哪个词
        self.freq = 0       # 记录单词出现的频率


class Trie:
    # 字典树
    # 初始化字典树
    def __init__(self):  # 初始化字典树
        self.root = Node()  # 初始化根节点（根节点不保存字符）
        self.res = []

    # 向字典树中插入一个单词
    def insert(self, word: str, freq: int) -> None:
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
        # 计入单词
        cur.word = word
        # 注意这里频率是可以累加的
        cur.freq += freq

    def get_word(self, node, path) -> None:
        """
        Time O(n)
        Space O(n)
        输入的node开始拿到整个字典树的word，并且加入大顶堆，保证频率最高的在最上面
        """
        # 走到底了
        if node.is_end:
            # 加入当前单词进入结果
            heapq.heappush(self.res, (-node.freq, path))

        # 遍历当前节点的所有children节点字符
        for k, v in node.children.items():
            # 加入path
            path += k
            self.get_word(v, path)
            # 这里记得要回溯，不然同一层的字符会一直叠加进path
            path = path[:-1]

        return

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


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie_tree = Trie()
        self.prefix = ''
        for sentence, time in zip(sentences, times):
            self.trie_tree.insert(sentence, time)

    def input(self, c: str) -> List[str]:
        """
        Time O(n * k + m * (n + k/m))
        Space O(k * (n * k + m))
        此题理解题意是最难的，这里需要注意的是，当输入词结束的时候，也要更新当前输入词的频率进字典树，同时没有结束的时候，输入的前缀是一直
        叠加的。详细见注释
        """
        # 存储结果
        res = []
        # 每次都要初始化字典树内，遍历path的结果
        self.trie_tree.res = []

        # 如果当前不是特殊字符，累加输入前缀
        if c != "#":
            self.prefix += c
        # 如果是特殊字符，说明结束查找
        else:
            # 更新当前前缀进字典树，同时频率累加 +1
            self.trie_tree.insert(self.prefix, 1)
            # 重新初始化前缀
            self.prefix = ""
            # 返回空list
            return res

        # 如果当前前缀存在于字典树内，开始找到所有可能组合
        if self.trie_tree.starts_with(self.prefix):
            # 起始节点
            start_node = self.trie_tree.root
            # 找到当前前缀走到的节点
            for ch in self.prefix:
                start_node = start_node.children[ch]
            # 开始遍历字典树，拿到所有path结果
            self.trie_tree.get_word(start_node, self.prefix)
            # 所有单词
            words = self.trie_tree.res
            # 弹出出现频率前三的单词，或者所有单词如果没有三个的话
            while words and len(res) < 3:
                res.append(heapq.heappop(words)[1])

        return res


obj = AutocompleteSystem(sentences=["i love you", "island", "iroman", "i love leetcode"], times=[5, 3, 2, 2])
print(obj.input(c='i'))
print(obj.input(c=" "))
print(obj.input(c="a"))
print(obj.input(c="#"))
print(obj.input(c='i'))
print(obj.input(c=" "))
print(obj.input(c="a"))
print(obj.input(c="#"))
print(obj.input(c='i'))
print(obj.input(c=" "))
print(obj.input(c="a"))
print(obj.input(c="#"))
