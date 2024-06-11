from typing import List


class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.res = set()

    def get_max_length(self, words):

        # 拿到候选词中的单词的最长长度
        max_length = float('-inf')
        for word in words:
            if len(word) > max_length:
                max_length = len(word)

        return max_length

    def backtracking(self, board, start_i, start_j, candidate_words, max_length, path, visited):
        m, n = len(board), len(board[0])
        # 判断当前path是否存在候选词内
        word = "".join(path)
        if word in candidate_words:
            # 用set来查重
            self.res.add(word)
        # 到达最大值长度，不需要继续添加词
        if len(path) == max_length:
            return
        # 遍历四个方向
        for direction in self.directions:
            # 下一个词
            next_i = start_i + direction[0]
            next_j = start_j + direction[1]
            # 越界，跳过
            if next_i < 0 or next_j < 0 or next_i >= m or next_j >= n:
                continue
            # 访问过，跳过
            if visited[next_i][next_j]:
                continue
            # 下一个加入path
            path.append(board[next_i][next_j])
            # 标记访问过
            visited[next_i][next_j] = True
            # 继续递归
            self.backtracking(board, next_i, next_j, candidate_words, max_length, path, visited)
            # 回溯
            path.pop()
            # 回溯
            visited[next_i][next_j] = False

        return

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Time O(m * n * m * n)
        Space O(m * n)
        最差情况，每个词都可能是起点，最大长度是整个board，也就是每个词要遍历整个board一次，此题用回溯加两个优化可以不需要字典树过所有TC。
        一个优化是如果当前字符在候选词中不是起始第一个词，那么我们不需要继续遍历。第二个优化是判断候选词中的最长长度，回溯的时候达到最长长度
        即可终止回溯。剩下的部分就是基础回溯写法，判断是否在候选词内，在的话就加入结果。注意不能有重复的结果，需要用set来存储结果再变成list。
        """
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                # 当前起始字符
                start_word = board[i][j]
                # 调出所有候选词
                candidate_words = [word for word in words if word[0] == start_word]
                # 如果有候选词才回溯判断
                if candidate_words:
                    # 防止走回头路，其实这里可以用特殊字符 * 来标记走过的地方，则不需要多开visited数组记录
                    visited = [[False] * n for _ in range(m)]
                    # 当前起始词标记
                    visited[i][j] = True
                    # 拿到最长长度
                    max_length = self.get_max_length(candidate_words)
                    # 开始递归，注意path要加入起始词
                    self.backtracking(board, i, j, set(candidate_words), max_length, [start_word], visited)

        # 转回去list
        return list(self.res)


class Node:  # 字符节点
    def __init__(self):  # 初始化字符节点
        self.children = {}  # 初始化子节点
        self.is_end = False  # is_end 用于标记单词结束
        self.word = ""      # 用于记录走到底的时候是什么word


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
        cur.word = word


class Solution2:
    def __init__(self):
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.res = set()

    def backtracking(self, node, board, i, j, m, n):
        # 判断当前ch是否存在当前字典树节点的children里面
        ch = board[i][j]
        # 如果不在，直接结束当前递归
        if ch not in node.children:
            return

        # 字典树里面children是字典，字符是key，所以我们要找当前当前节点的字符应该在children这个字典里面
        next_node = node.children[ch]
        # 如果这个上面找到的这个字符对应的节点没有children，同时is end说明已经找到了一个单词，加入结果
        if next_node.is_end:
            self.res.add(next_node.word)

        # 标记访问过，不走回头路
        board[i][j] = "*"
        # 遍历四个方向
        for direction in self.directions:
            # 下一个词
            next_i = i + direction[0]
            next_j = j + direction[1]
            # 越界，跳过
            if next_i < 0 or next_j < 0 or next_i >= m or next_j >= n:
                continue
            # 访问过，跳过
            if board[next_i][next_j] == "*":
                continue
            # 继续递归
            self.backtracking(next_node, board, next_i, next_j, m, n)
        # 记得离开当前节点的时候要回溯，不然下个词作为起始点的时候可能出现之前访问过不能再次访问的情况
        board[i][j] = ch

        return

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Time O(m * 4 * 3^l)
        Space O(n)
        标准的字典树加回溯写法，我们先把所有word存入字典树，然后再每个点都作为起点的可能情况下遍历board，每次递归查找当前字符在不在字典树里面，
        在的话就继续下一步递归，直到找到终点词。如果不在就直接结束当前递归。
        """
        m, n = len(board), len(board[0])
        # 初始化字典树
        trie_tree = Trie()
        # 把每个word加入字典树
        for word in words:
            trie_tree.insert(word)

        for i in range(m):
            for j in range(n):
                # 开始遍历每个字符作为第一个字母在字典树内
                self.backtracking(trie_tree.root, board, i, j, m, n)

        # 转回去list
        return list(self.res)


s1 = Solution2()
print(s1.findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                   words=["oath", "pea", "eat", "rain"]))
s2 = Solution()
print(s2.findWords(board=[["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]],
                   words=["oa", "oaa"]))
s3 = Solution()
print(s3.findWords(board=[["a", "a"]], words=["aaa"]))
