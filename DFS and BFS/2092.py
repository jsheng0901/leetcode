import heapq
from collections import defaultdict, deque
from typing import List


class Solution1:
    def bfs(self, graph, earliest, firstPerson):
        # Queue for BFS. It will store (person, time of knowing the secret)
        queue = deque()
        # 初始状态两个点加入列队
        queue.append((0, 0))
        queue.append((firstPerson, 0))

        while queue:
            # 当前列队头
            person, time = queue.popleft()
            for t, nei in graph[person]:
                # 如果当前下一个的meeting时间大于当前节点的meeting时间，并且小于最早完成时间
                if time <= t < earliest[nei]:
                    earliest[nei] = t
                    queue.append((nei, t))

        return earliest

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        """
        Time O(m * (n + m))     n -> number of people   m -> number of meetings
        Space O(n + m)
        参考：https://leetcode.com/problems/find-all-people-with-secret/editorial/
        先构建双向图，这里每次找下一个邻居点的时候，需要确定下一个点是不是开始meeting的时间比当前这个晚，并且确定下一个点的最早meeting时间
        是不是大于当前时间，这样才可以确定当前下一个meeting的最早时间，保证其它相连接的meeting可以传播到。这题相当于是 Dijkstra's 的变形。
        我们访问node如果当前距离可以更短，这里是当前时间可以更早。
        """
        # For every person, store the time and label of the person met.
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))

        # Earliest time at which a person learned the secret
        # as per current state of knowledge. If due to some new information,
        # the earliest time of knowing the secret changes, we will update it
        # and again process all the people whom he/she meets after the time
        # at which he/she learned the secret.
        earliest = [float('inf')] * n
        earliest[0] = 0
        earliest[firstPerson] = 0

        # BFS find each person earliest meeting time
        earliest = self.bfs(graph, earliest, firstPerson)

        # 如果访问到，则不等于初始值
        return [i for i in range(n) if earliest[i] != float('inf')]


class Solution2:
    def dfs(self, graph, node, time, earliest):
        # DFS 写法，处理当前节点的状态先
        earliest[node] = time
        for t, nei in graph[node]:
            # 如果当前下一个的meeting时间大于当前节点的meeting时间，并且小于最早完成时间，满足条件在进入下一个节点
            if time <= t < earliest[nei]:
                self.dfs(graph, nei, t, earliest)

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        """
        Time O(m * (n + m))     n -> number of people   m -> number of meetings
        Space O(n + m)
        逻辑同BFS，只是换成DFS写。
        """
        # For every person, store the time and label of the person met.
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))

        # Earliest time at which a person learned the secret
        # as per current state of knowledge. If due to some new information,
        # the earliest time of knowing the secret changes, we will update it
        # and again process all the people whom he/she meets after the time
        # at which he/she learned the secret.
        earliest = [float('inf')] * n

        # DFS find each person earliest meeting time，这里需要两个初始节点
        self.dfs(graph, 0, 0, earliest)
        self.dfs(graph, firstPerson, 0, earliest)

        # 如果访问到，则不等于初始值
        return [i for i in range(n) if earliest[i] != float('inf')]


class Solution3:
    def bfs(self, graph, firstPerson, n):
        # Priority Queue for BFS. It stores (time secret learned, person)
        # It pops the person with the minimum time of knowing the secret.
        pq = []
        heapq.heappush(pq, (0, 0))
        heapq.heappush(pq, (0, firstPerson))

        # Visited array to mark if a person is visited or not.
        # We will mark a person as visited after it is dequeued
        # from the queue.
        # 注意这里一定要弹出后才Mark，这是和传统BFS写法不一样的地方，而不是在加入列队的时候Mark，因为同一个点可以重复访问，
        # 需要找到重复访问中meeting时间最小的那个，然后再加入列队的时候就判断的话，同一个点和容易忽视下一个更早访问的时间。测试4是例子。
        visited = [False] * n

        while pq:
            # 当前列队头
            time, person = heapq.heappop(pq)
            # 弹出后才Mark访问过
            if visited[person]:
                continue
            visited[person] = True
            for t, nei in graph[person]:
                # 如果当前下一个的meeting时间大于当前节点的meeting时间，并且小于上一个的完成时间
                if visited[nei] is False and t >= time:
                    # 此时加入列队
                    heapq.heappush(pq, (t, nei))

        return visited

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        """
        Time O((n + m) * log(n + m) + n * m))    n -> number of people   m -> number of meetings
        Space O(n + m)
        参考：https://leetcode.com/problems/find-all-people-with-secret/editorial/
        先构建双向图，这里每次找下一个邻居点的时候，需要确定下一个点是不是开始meeting的时间比当前这个晚，并且确定下一个点的最早meeting时间
        是不是大于当前时间，这样才可以确定当前下一个meeting的最早时间，保证其它相连接的meeting可以传播到。这里利用优先列队的优势，
        每次访问的时候是先弹出meeting时间最早的那个。
        """
        # For every person, store the time and label of the person met.
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))

        # Priority Queue for BFS，记录每个访问的点
        visited = self.bfs(graph, firstPerson, n)

        # 如果访问到说明可以reach到
        return [i for i in range(n) if visited[i]]


s = Solution3()
print(s.findAllPeople(n=6, meetings=[[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson=1))
print(s.findAllPeople(n=4, meetings=[[3, 1, 3], [1, 2, 2], [0, 3, 3]], firstPerson=3))
print(s.findAllPeople(n=5, meetings=[[3, 4, 2], [1, 2, 1], [2, 3, 1]], firstPerson=1))
print(s.findAllPeople(n=4, meetings=[[0, 1, 4], [1, 3, 3], [2, 1, 2]], firstPerson=2))
