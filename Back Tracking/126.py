from collections import defaultdict, deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: [str]) -> [[str]]:
        """
        O(n*k^2 + alpha) time, O(n) for bfs n node traversal, O(k^2) for find neighbors for each word, alpha for BK path
        O(n*k) space, for build set and queue
        first used bfs build each node possible neighbors graph, second backtracking all path in graph and find valid
        """
        self.adj_map = defaultdict(set)
        result = []

        if endWord not in wordList:
            return []

        # build_adjacency_map
        self.bfs(beginWord, set(wordList))

        self.traverse_and_backtrack(beginWord, endWord, [beginWord], result)
        return result

    def findNeighbors(self, cur_word, word_list):
        neighbors = set()
        for i in range(len(cur_word)):
            for char in 'qwertyuiopasdfghjklzxcvbnm':
                next_word = cur_word[:i] + char + cur_word[i + 1:]
                if next_word in word_list:
                    neighbors.add(next_word)
        return neighbors

    def bfs(self, begin_word, word_list):
        queue = deque()
        queue.append(begin_word)

        while queue:
            word_list = word_list.difference(set(queue))
            layer_size = len(queue)
            for l in range(layer_size):
                cur_word = queue.popleft()
                neighbors = self.findNeighbors(cur_word, word_list)
                for neighbor in neighbors:
                    self.adj_map[cur_word].add(neighbor)
                    queue.append(neighbor)

    def traverse_and_backtrack(self, source, dest, cur_path, result):
        if source == dest:
            result.append(cur_path.copy())

        if source not in self.adj_map:
            return

        for word in self.adj_map[source]:
            cur_path.append(word)
            self.traverse_and_backtrack(word, dest, cur_path, result)
            cur_path.pop()  # backtrack