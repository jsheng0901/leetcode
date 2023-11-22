from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.count -= 1

    def get_num_set(self):
        return self.count


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        """
        Time O(n + nlog(n))
        Space O(n)
        并查集模版题目，这里需要注意的是，找最早的时间，需要先把logs sort一遍从小到大根据第一个元素timestamp。
        之后就一直union两个节点，直到整个graph成为一个整体，及count = 1。
        """
        # sorted logs 根据 timestamp
        logs = sorted(logs, key=lambda x: x[0])
        uf = UnionFind(n)

        for log in logs:
            # 当前log
            time, x, y = log[0], log[1], log[2]
            # union起来
            uf.union(x, y)
            # 如果已经是一个graph，说明找到最早的时间，直接结束
            if uf.get_num_set() == 1:
                return time

        return -1


s = Solution()
print(s.earliestAcq(logs=[[9, 3, 0], [0, 2, 1], [8, 0, 1], [1, 3, 2], [2, 2, 0], [3, 3, 1]], n=4))
