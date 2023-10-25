from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        self.parent[root_x] = root_y
        self.count -= 1

    def connected(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        return root_x == root_y

    def get_num_set(self):

        return self.count


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        Time O(n^2)
        Space O(n)
        并查集的应用，每个石头看做一个点，如果符合行或者列相等，则链接这两个石头，总共多少石头 - 链接后集合的个数，就是最多移除的石头个数。
        """
        # 初始化并查集
        uf = UnionFind(len(stones))

        # 这里我们遍历所有可能的石头组合
        for i in range(len(stones)):
            stone1 = stones[i]
            for j in range(i + 1, len(stones)):
                stone2 = stones[j]
                # 判断是否可以链接，如果可以链接则union起来
                if stone1[0] == stone2[0] or stone1[1] == stone2[1]:
                    uf.union(i, j)

        # 返回最多移除的石头个数
        return len(stones) - uf.count
