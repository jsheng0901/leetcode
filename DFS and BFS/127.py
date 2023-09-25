from collections import deque, defaultdict
from typing import List


class Solution1:
    def findNeighbors(self, cur_word, word_list):
        neighbors = set()
        for i in range(len(cur_word)):
            for char in 'qwertyuiopasdfghjklzxcvbnm':
                next_word = cur_word[:i] + char + cur_word[i + 1:]
                if next_word in word_list:
                    neighbors.add(next_word)
        return neighbors

    def bfs(self, begin_word, end_word, word_list):
        queue = deque()
        queue.append(begin_word)
        length = 0
        while queue:
            word_list = word_list.difference(set(queue))
            layer_size = len(queue)
            length += 1
            for l in range(layer_size):
                cur_word = queue.popleft()
                neighbors = self.findNeighbors(cur_word, word_list)
                for neighbor in neighbors:
                    self.adj_map[cur_word].add(neighbor)
                    queue.append(neighbor)
                    if neighbor == end_word:
                        return length + 1
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        """
        Time O(n*k^2), O(n) for bfs n node traversal, O(k^2) for find neighbors for each word
        Space O(n*k), for build set and queue
        first used bfs build each node possible neighbors graph, second backtracking all path in graph and find valid
        """
        self.adj_map = defaultdict(set)

        if endWord not in wordList:
            return 0

        # build_adjacency_map and return result
        return self.bfs(beginWord, endWord, set(wordList))


class Solution2:
    def bfs(self, beginWord, endWord, word_set, step_mapping):
        # 初始化
        queue = [beginWord]
        step_mapping[beginWord] = 1

        while queue:
            # 弹出第一个单词
            word = queue.pop(0)
            # 同时弹出走到这一层的step
            step = step_mapping[word]
            # 找到所有邻居单词
            for i in range(len(word)):
                word_list = list(word)
                for j in range(26):
                    word_list[i] = chr(ord('a') + j)
                    new_word = "".join(word_list)
                    # 如果下一个单词是结尾词，直接返回新的step
                    if new_word == endWord:
                        return step + 1
                    # 当单词存在word set里面并且没有访问过的时候，我们进入下一个单词
                    if new_word in word_set and new_word not in step_mapping:
                        queue.append(new_word)
                        step_mapping[new_word] = step + 1

        # 没有找到结尾词在word set里面，返回0
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Time O(n * len(word) * 26) 每个bfs临近node每个字母要找一遍26个字母
        Space O(n * len(word)) queue和mapping
        BFS题型，注意这里一定要先把 word list 转化成 word set 不然后面check存不存在的时候会超时。用一个dictionary来记录每一步的单次的
        走到的step，也就是二叉树里面的每层的深度。
        """
        # 注意一定要转换成set，后续会快很多
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in wordList:
            return 0

        # 记录每个单次走到的step，同时查重，不走回头路
        step_mapping = {}

        step = self.bfs(beginWord, endWord, word_set, step_mapping)

        return step


s = Solution2()
print(s.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
print(s.ladderLength(beginWord="a", endWord="c", wordList=["a", "b", "c"]))
