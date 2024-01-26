from collections import defaultdict, OrderedDict
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))

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

    def connected(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        return root_x == root_y


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        """
        Time uf: O(n) + orderdict: O(n * log(n)) + loop: O(n) -> O(n * log(n))
        Space O(n)
        核心思想，对应good path来说我们只需要找到一个path里面node的值全都小于起点和重点就可，也就是我们需要在一个图里面找到sub-graph
        并计算出每个sub-graph的component有多少个节点，每个component里面的path则为 (n * (n + 1)) / 2。
        所以我们从value小到大开始构建sub-graph，并且每次计算当前sub-graph里面的component有多少个点和多少个good path，
        这里用UF一直build graph，并且用UF的find来找component的个数。
        """
        graph = defaultdict(list)
        value_2_node = defaultdict(list)
        n = len(vals)
        # 构建无向图
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # 构建value到index也就node的map
        for i, v in enumerate(vals):
            value_2_node[v].append(i)

        # 这里需要sorted一下上面的map by key，才能后续做到从小到大遍历
        value_2_node_sorted = OrderedDict(sorted(value_2_node.items()))

        # 初始化 UF
        uf = UnionFind(n)
        good_path = 0

        # 开始从小到大遍历value，对于同一个value的node构建sub-graph
        for nodes in value_2_node_sorted.values():
            # 对于每个node构建和塔的邻居的sub-graph
            for node in nodes:
                # 这里邻居只选比自己value小的节点，因为我们要good path
                for nei in graph[node]:
                    # 找到比自己小的，UF链接起来
                    if vals[node] >= vals[nei]:
                        uf.union(node, nei)

            # 遍历完当前value下的所有节点也就是构建完所有sub-graph后，开始计算每个sub-graph小的component里面node的个数
            group = defaultdict(int)
            for n in nodes:
                # 用UF里面的find找到每个component的节点个数
                group[uf.find(n)] += 1
            # 遍历每个sub-graph计算里面的good path
            for size in group.values():
                good_path += int((size * (size + 1)) / 2)

        return good_path


s = Solution()
print(s.numberOfGoodPaths(vals=[1, 3, 2, 1, 3], edges=[[0, 1], [0, 2], [2, 3], [2, 4]]))
