from collections import deque, defaultdict


class Solution:
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
        O(n*k^2) time, O(n) for bfs n node traversal, O(k^2) for find neighbors for each word
        O(n*k) space, for build set and queue
        first used bfs build each node possible neighbors graph, second backtracking all path in graph and find valid
        """
        self.adj_map = defaultdict(set)

        if endWord not in wordList:
            return 0

        # build_adjacency_map and return result
        return self.bfs(beginWord, endWord, set(wordList))


