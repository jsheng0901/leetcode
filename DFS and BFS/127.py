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
        BFS题型，注意这里一定要先把 word list 转化成 word set 不然后面check存不存在的时候会超时，原因是因为set是hash map，check存在的
        时候是O(1)，然而List是数组，check存在的时候是O(n)，时间上大大提高了检查是否存在的速度。再用一个dictionary来记录每一步的单次的
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


class Solution3:
    def bfs(self, beginWord, endWord, word_set):

        queue = [(beginWord, 1)]
        visited = set()
        visited.add(beginWord)

        while queue:
            word, step = queue.pop(0)
            # 这里可以在当前节点判断是否是结束词，也可以在下面下一个节点的时候判断
            # if word == endWord:
            #     return step
            for i in range(len(word)):
                word_list = list(word)
                for j in range(26):
                    word_list[i] = chr(ord('a') + j)
                    new_word = "".join(word_list)
                    # 在这里判断就是可以少一步判断下一个词是否在候选词里面和是否被访问过，不过这些判断都是set，也就是都是O(1)的操作
                    if new_word == endWord:
                        return step + 1
                    if new_word in word_set and new_word not in visited:
                        queue.append((new_word, step + 1))
                        visited.add(new_word)

        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Time O(n * len(word) * 26) 每个bfs临近node每个字母要找一遍26个字母
        Space O(n * len(word)) queue和visited
        同上的思路，只是我们不用mapping去check状态，用visited集合去check是否访问过，同时queue存储当前节点走到的时候step的距离。
        本质上就是判断node是否有走回头路，并且node要存储当前的状态。
        """
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in wordList:
            return 0

        step = self.bfs(beginWord, endWord, word_set)

        return step


class Solution4:
    def visited_node(self, queue, visited, others_visited, word_set):
        word = queue.pop(0)
        # if word in others_visited:
        #     return visited[word] + others_visited[word]
        for i in range(len(word)):
            word_list = list(word)
            for j in range(26):
                word_list[i] = chr(ord('a') + j)
                new_word = "".join(word_list)
                if new_word in others_visited:
                    return visited[word] + others_visited[new_word]
                if new_word in word_set and new_word not in visited:
                    queue.append(new_word)
                    visited[new_word] = visited[word] + 1

        return None

    def bfs(self, beginWord, endWord, word_set):

        begin_queue = [beginWord]
        end_queue = [endWord]
        begin_visited = {beginWord: 1}
        end_visited = {endWord: 1}
        min_step = float('inf')

        while begin_queue and end_queue:
            if len(begin_queue) <= len(end_queue):
                ans = self.visited_node(begin_queue, begin_visited, end_visited, word_set)
            else:
                ans = self.visited_node(end_queue, end_visited, begin_visited, word_set)

            if ans:
                min_step = min(min_step, ans)

        return 0 if min_step == float('inf') else min_step

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Time O(n * len(word) * 26) 每个bfs临近node每个字母要找一遍26个字母
        Space O(n * len(word)) queue和visited
        这里其实时间上会更快一点，因为是双向BFS，本质上就是两个BFS一个接着一个走，如果遇到了对方走过的节点，说明找到了一条path，记录距离，
        统计最短的距离，这里本人觉得需要遍历所有可能的path才能找到最短距离，因为当遇到另个BFS访问过的节点时候，不确定是否就是最短距离的节点，
        因为可能另一个BFS多走了好几步，当遇到交集的时候并不是另一个BFS的最短距离状态。
        本质上是因为，BFS当graph是确定的时候那么一定是最短距离，但是这里我们在构建graph，因为每个节点是单词接龙，即使是同一个step但是构建的
        方式不一样会导致最后的graph不一样，所以要遍历所有可能的path才能找到最短的距离。
        """
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in wordList:
            return 0

        step = self.bfs(beginWord, endWord, word_set)

        return step


s = Solution4()
print(s.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
print(s.ladderLength(beginWord="a", endWord="c", wordList=["a", "b", "c"]))
print(s.ladderLength(beginWord="hbo", endWord="qbx",
                     wordList=["abo", "hco", "hbw", "ado", "abq", "hcd", "hcj", "hww", "qbq", "qby", "qbz", "qbx",
                               "qbw"]))
