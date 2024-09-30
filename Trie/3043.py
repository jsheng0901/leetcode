from typing import List


class Solution1:
    def prefix_length(self, x, y):
        string_x = str(x)
        string_y = str(y)
        p1 = 0
        p2 = 0
        # 双指针，计算当前两个字符串的最长公共前缀
        while p1 < len(string_x) and p2 < len(string_y):
            if string_x[p1] == string_y[p2]:
                p1 += 1
                p2 += 1
            else:
                break

        return p1

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Time O(m * n * d) -> O(m * n)
        Space O(1)
        暴力解法，找到所有两两组合，然后找到所有公共前缀，并且同时更新最长长度。TLE明显。
        """
        longest_prefix = 0
        # 找到所有组合
        for x in arr1:
            for y in arr2:
                # 找到当前组合的公共前缀长度
                length = self.prefix_length(x, y)
                # 更新全局最长长度
                longest_prefix = max(longest_prefix, length)

        return longest_prefix


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

    # 查找字典树中是否存在一个前缀
    def starts_with_get_length(self, prefix: str) -> int:
        """
        Time O(n)
        Space O(1)
        遍历prefix这个word，同时拿到最长长度
        """
        # 记录prefix的长度
        length = 0
        cur = self.root
        for ch in prefix:  # 遍历前缀中的字符
            if ch not in cur.children:  # 如果当前节点的子节点中，不存在键为 ch 的节点
                break
            cur = cur.children[ch]  # 令当前节点指向新建立的节点，然后继续查找下一个字符
            length += 1     # 前缀记录长度

        return length


class Solution2:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Time O(m * d + n * d) -> O(m + n)
        Space O(m * d)
        字典树的模版题，把数组1里面的所有数存进字典树，数组2里面每个数去数组1的字典树里面找最长公共前缀，同时更新全局最长前缀。
        """
        # 构建字典树
        trie = Trie()
        for x in arr1:
            # 数组1里面的数都存进字典树
            trie.insert(str(x))

        longest_prefix = 0
        for y in arr2:
            # 计算数组2里面的当前数在数组1字典树里的前缀长度
            prefix_length = trie.starts_with_get_length(str(y))
            # 更新全局最长前缀长度
            longest_prefix = max(longest_prefix, prefix_length)

        return longest_prefix


s = Solution2()
print(s.longestCommonPrefix(arr1=[1, 10, 100], arr2=[1000]))
print(s.longestCommonPrefix(arr1=[1, 2, 3], arr2=[4, 4, 4]))
