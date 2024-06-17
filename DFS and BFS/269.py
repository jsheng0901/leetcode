from collections import defaultdict, Counter
from typing import List


class Solution:
    def bfs(self, graph, in_degree):
        # BFS 标准的拓扑排序写法
        # 先把所有入度是0的加入进列队
        queue = []
        for k, v in in_degree.items():
            if v == 0:
                queue.append(k)

        res = ""
        # 开始执行 BFS 算法
        while queue:
            front = queue.pop(0)
            # 加入结果
            res += front
            # 遍历邻居节点
            for nei in graph[front]:
                # 入度 -1
                in_degree[nei] -= 1
                # 当入度没有的时候才进此节点
                if in_degree[nei] == 0:
                    queue.append(nei)

        return res

    def alienOrder(self, words: List[str]) -> str:
        """
        Time O(c + u + min(u^2, n)) --> O(c)   c -> total word in words，n -> number of string in words， u -> unique chr
        Space O(u + min(u^2, n)) --> O(1) since u it's fix 26 characters
        此题的难点在于如何构建graph，然后用BFS进行拓扑排序输出，此时输出顺序就是我们要的单词组成的word顺序。详细见注释。
        """
        # 构建graph，用set，因为可能会出现重复计算的节点和入度
        graph = defaultdict(set)
        # 对于没有入度的节点要构建一个0，因为这里是字典构建入度，不然没有初始节点
        in_degree = Counter({c: 0 for word in words for c in word})
        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]
            # 遍历每一对word
            for f, s in zip(first, second):
                # 如果当前单词不相等，找到一个顺序
                if f != s:
                    # 注意这里为了防止重复计算入度，需要先判断一下之前是否出现过
                    if s not in graph[f]:
                        # 加入图 first --> second
                        graph[f].add(s)
                        # second 入度 +1
                        in_degree[s] += 1
                    # 后续的单词不用判断没有意义，直接结束
                    break
            # 这里有一个for loop 的 else 用法，意思是是如果loop里面没有遇到break，则执行下面逻辑
            else:
                # 如果判断完后前面的词都相等，如果第二个词长度小于第一个词，说明是第一个词的前缀，
                # 直接返回空string，因为没有足够的信息判断单词顺序
                if len(second) < len(first):
                    return ""

        # BFS拓扑排序写法
        res = self.bfs(graph, in_degree)
        # 最后判断一下是不是所有的unique字符都进入结果了，如果不是说明有环，则返回空string
        return res if len(res) == len(in_degree) else ""


class Solution2:
    def __init__(self):
        self.path = {}
        self.visited = {}
        self.res = []
        self.cycle = False

    def dfs(self, node, graph):
        # DFS 标准的拓扑排序写法
        # 发现环，直接结束
        if node in self.path and self.path[node]:
            self.cycle = True
            return
        # 发现环，或者已经访问过，等价于走到终点，直接结束
        if self.cycle or (node in self.visited and self.visited[node]):
            return

        # 前序遍历位置，记录当前节点访问过
        self.path[node] = True
        self.visited[node] = True

        for nei in graph[node]:
            self.dfs(nei, graph)

        # 后序遍历位置，记录离开当前节点，同时加入result结果数组
        self.path[node] = False
        self.res.append(node)

        return

    def alienOrder(self, words: List[str]) -> str:
        """
        Time O(c + u + min(u^2, n)) --> O(c)   c -> total word in words，n -> number of string in words， u -> unique chr
        Space O(u + min(u^2, n)) --> O(1) since u it's fix 26 characters
        同思路1，只是这里用DFS写法来写。
        """
        # 这里graph的构建要用list，需要记录每个单词对应的指向，即使是空的list，因为后续要遍历所有节点来判断是否有环在graph里面
        graph = {c: [] for word in words for c in word}
        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]
            for f, s in zip(first, second):
                if f != s:
                    if s not in graph[f]:
                        graph[f].append(s)
                    break
            else:
                if len(second) < len(first):
                    return ""
        # 对于所有的在图内的节点也就是所有unique字符，都要判断一次是否有环
        for key in graph.keys():
            self.dfs(key, graph)
        # 注意DFS的后续遍历返回的是拓扑排序后的倒序，所以需要reverse一下整个string，
        # 或者还有个办法就是构建graph的时候反过来构建，则不需要reverse，因为reverse是O(c)的操作所以不影响整体时间复杂度
        return "" if self.cycle else "".join(self.res[::-1])


s1 = Solution2()
print(s1.alienOrder(words=["wrt", "wrf", "er", "ett", "rftt"]))
s2 = Solution2()
print(s2.alienOrder(words=["z", "x"]))
s3 = Solution2()
print(s3.alienOrder(words=["z", "x", "z"]))
s4 = Solution2()
print(s4.alienOrder(words=["z", "z"]))
s5 = Solution2()
print(s5.alienOrder(words=["ac", "ab", "zc", "zb"]))
s6 = Solution2()
print(s6.alienOrder(words=["abc", "ab"]))
