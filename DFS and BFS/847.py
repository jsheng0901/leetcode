from typing import List


class Solution1:
    def bfs(self, graph, node):
        # 构建visited数组记录访问每个点的状态
        visited = [False] * len(graph)
        # 初始化第一个点访问过
        visited[node] = True
        # 初始化路径
        step = 0
        # 用三元素记录每个点的状态分别是: (当前节点，走到当前节点的步长，访问到当前节点的时候访问所有点的状态)
        queue = [(node, step, visited)]

        while queue:
            size = len(queue)
            for i in range(size):
                # 弹出栈顶，也就是处理访问当前节点的时候
                top, step, visited = queue.pop(0)
                # 如果当前节点对应的访问其它所有节点的状态都是true，说明全都访问过，则直接返回走到当前节点的步长
                if all(visited):
                    return step
                # 遍历邻居节点
                for nei in graph[top]:
                    # 这里要备份一下，因为Python里面数组是可变的
                    visited_copy = visited.copy()
                    # 标记邻居节点也为访问过
                    visited_copy[nei] = True
                    # 邻居节点状态加入栈
                    queue.append((nei, step + 1, visited_copy))

        return

    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        Time o(n^2)
        Space O(n)
        每个点进行BFS遍历，找到每个点作为起始点的时候BFS返回的最小路径。每个点BFS的时候用一个数组记录从这个点BFS的时候
        走过的每个其它点的状态。当都是true的时候以为着访问完所有点，返回走了多少步。也就是加一个visited数组记录每个点当前是否被遍历。
        不过这个方法会超时，因为这里BFS的时候可以走重复的节点，所以会出现很多次重复遍历某个点的状况。
        """
        # 全局最小path
        min_step = float('inf')
        # 遍历每个点作为起始点的状态
        for i in range(len(graph)):
            step = self.bfs(graph, i)
            min_step = min(min_step, step)

        return min_step


class Solution2:
    def bfs(self, graph, node):
        # 初始化栈内元素，为起点节点，这里用二进制转换来存储原本为visited的每个点的访问状态数组
        queue = [(node, 0, 1 << node)]
        # 用另应该visited集合来记录当前节点在当前其它节点的访问状态在是否有访问过，
        # ex: {1, [1, 1, 1, 0]} 翻译过来就是，当前节点 1，访问过其它节点 0，1，2，但是3没有访问过。
        visited = {node, 1 << node}

        while queue:
            size = len(queue)
            for i in range(size):
                # 当前节点状态
                top, step, traveled = queue.pop(0)
                # 如果所有节点都访问过，则返回步长
                if traveled == (1 << len(graph)) - 1:
                    return step
                for nei in graph[top]:
                    # 标记邻居节点也为访问过
                    traveled_copy = traveled | (1 << nei)
                    # 如果邻居节点对应的状态出现过在visited集合内，说明再次访问一定不会是最短路径，所有只有没有出现过的才会入栈
                    if (nei, traveled_copy) not in visited:
                        # 邻居节点状态加入栈
                        queue.append((nei, step + 1, traveled_copy))
                        # 邻居节点状态加入已访问集合
                        visited.add((nei, traveled_copy))

        return

    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        Time O(n^2) worse case，大部分情况比第一种快，因为第一种一定有重复访问记录
        Space O(n)
        第一个解法的主要问题是因为visited是数组，没法hash，
        因此无法使用另一个visited记录 (node, traveled) 是否出现过来减少重复访问的过的搜索空间。
        解决办法是将这个数组变为字符串 → 更进一步可以变为二进制字符串 → 又可以用一位十进制数表示，这样既可以hash，又进行了状态压缩。
        具体来说，如果十进制数 == 2^N - 1 则代表所有节点都被访问到了，具体实现 if traveled == (1 << N) - 1
        初始化为出发节点的二进制对应的十进制，1<<node（左移i位代表 times 2^i）
        记录traveled信息的增加，traveled_copy = traveled | (1 << nei)
        """
        # 这里同上
        min_step = float('inf')

        for i in range(len(graph)):
            step = self.bfs(graph, i)
            min_step = min(min_step, step)

        return min_step
