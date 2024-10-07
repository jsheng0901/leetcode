from typing import List


class UnionFind:
    def __init__(self, n: int):
        # 初始化为空，而不是指向自己，因为一开始都是水，也就是说没有节点
        self.parent = [-1 for _ in range(n)]
        # 平衡并查集用的数组，记录大小
        self.size = [0 for _ in range(n)]
        # 记录component个数，也就是陆地个数
        self.count = 0

    def add_land(self, x):
        # 添加陆地，如果已经是陆地了，则跳过
        if self.parent[x] >= 0:
            return
        # 节点指向自己，表示此节点是陆地
        self.parent[x] = x
        # 对应的个数更新
        self.count += 1

    def is_land(self, x):
        # 判断是不是陆地
        return self.parent[x] >= 0

    def number_of_islands(self):
        # 返回当前陆地个数
        return self.count

    def find(self, x):
        # 找到根节点
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        # 合并两个根节点
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        # 引入平衡数组记录重量后，小树接到大树下面，较平衡
        # if self.size[root_x] > self.size[root_y]:
        #     self.parent[root_y] = root_x
        #     self.size[root_x] += self.size[root_y]
        # else:
        #     self.parent[root_x] = root_y
        #     self.size[root_y] += self.size[root_x]

        # 也可以写简版的合并，不太影响速度
        self.parent[root_x] = root_y
        # 对应的component个数-1
        self.count -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        """
        Time O(m * n + l)   l -> number of positions
        Space O(m * n)
        此题应该是并查集的改编，难点在一开始所有节点都指向空节点，而不是自己，换句话来说一开始是水的时候并不是节点，翻转成陆地之后才是节点，
        变成陆地之后，节点指向自己。然后查找四周是否是陆地，如果是陆地则进行合并，同时更新陆地个数，这里初始化的陆地为component的个数是0。
        还有个trick是，把二维数组变成一位数组，new_x = x * n + y，n 是 column个数。
        """
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # 构建一维的并查集
        uf = UnionFind(m * n)
        ans = []

        for x, y in positions:
            # 转二维空间为一维
            land_position = x * n + y
            # 添加为陆地
            uf.add_land(land_position)

            # 遍历四个邻居
            for direction in directions:
                next_x = x + direction[0]
                next_y = y + direction[1]
                # 一维空间
                next_land_position = next_x * n + next_y
                # 二维空间中越界
                if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                    continue
                # 不是陆地，则不需要union
                if uf.is_land(next_land_position) is False:
                    continue

                # union起来这两个节点
                uf.union(next_land_position, land_position)
            # 加入结果
            ans.append(uf.number_of_islands())

        return ans


s = Solution()
print(s.numIslands2(m=3, n=3, positions=[[0, 0], [0, 1], [1, 2], [2, 1]]))
print(s.numIslands2(m=1, n=1, positions=[[0, 0]]))
