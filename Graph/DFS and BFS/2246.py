from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.path = 0

    def build_graph(self, parent):
        # 构建无向图
        graph = defaultdict(list)

        for i, v in enumerate(parent):
            # 需要注意这里根节点直接跳过
            if i == 0:
                continue
            graph[i].append(v)
            graph[v].append(i)

        return graph

    def dfs(self, node, graph, parent, s):
        # 当前节点所有子节点返回值里面对应的最长的两个值
        top_1_distance, top_2_distance = 0, 0
        # 当前节点所有无法走通子节点返回值里的最长的值
        unconnected_distance = 0
        # 遍历邻居节点
        for nei in graph[node]:
            # 这里直接把父节点传过来，方便判断是否走回头路，不需要visited数组
            if nei == parent:
                continue

            # 如果当前节点无法走通
            if s[nei] == s[node]:
                # 当前节点拿到的子节点返回值，此时不用 +1， 因为本身这个edge不能计算进去
                distance = self.dfs(nei, graph, node, s)
                # 更新对应的长度
                if distance > unconnected_distance:
                    unconnected_distance = distance
            # 如果当前节点可以走通，同1245题思路
            else:
                distance = self.dfs(nei, graph, node, s) + 1

                # 后续遍历位置，用两个指针来接住最长的两个距离
                # 如果大于最长的距离，则更新两个距离
                if distance > top_1_distance:
                    # 注意这里一定要先更新第二个距离，再更新第一个，否则顺序颠倒的话第二个距离会等于第一个距离
                    top_2_distance = top_1_distance
                    top_1_distance = distance
                    # 或者采用这种swap的形式写，同一行更新
                    # top_1_distance, top_2_distance = distance, top_1_distance
                # 如果大于第二个，则只更新第二个距离
                elif distance > top_2_distance:
                    top_2_distance = distance

        # 更新最长路径，这里用三种可能
        self.path = max(self.path, top_1_distance + top_2_distance, unconnected_distance)

        # 返回最长的距离，一定是可以走通的里面最长的值
        return top_1_distance

    def longestPath(self, parent: List[int], s: str) -> int:
        """
        Time O(n)
        Space O(n)
        整体思路和1245一样，找到最长的两个子节点的返回值，然后同时更新最长路径，返回最大的子节点路径，需要注意的是，这里要判断一下每次两个
        节点是否是一样的label，如果是一样的label，那么我们就记录下来这个不能走的path的最大值路径，因为可能这个就是最长路径，如果不是一样的
        label，那么就和1245一样需要在可以走的path里面找到最长的两个path，加起来就是当前最长path。返回值一定是可以走的路径，不能返回不能走
        的路径，因为父节点无法走下去。
        """
        graph = self.build_graph(parent)

        self.dfs(0, graph, 0, s)

        # 结果要 +1，因为记录的是edge，对应节点要多一个
        return self.path + 1


class Solution2:
    def __init__(self):
        self.ans = 0

    def build_graph(self, parent):
        # 同思路1
        graph = defaultdict(list)

        for i, v in enumerate(parent):
            if i == 0:
                continue
            graph[i].append(v)
            graph[v].append(i)

        return graph

    def dfs(self, node, graph, parent, s):
        # 当前节点所有子节点返回值里面对应的最多的两个值
        top_1, top_2 = 0, 0
        # 遍历邻居节点
        for nei in graph[node]:
            # 这里直接把父节点传过来，方便判断是否走回头路，不需要visited数组
            if nei == parent:
                continue
            # 得到子节点的返回值
            distance = self.dfs(nei, graph, node, s)

            # 如果label不一样，才进行更新两个指针，如果一样，直接跳过这个路径，因为对应的节点个数已经在子节点的时候更新过了
            if s[nei] != s[node]:
                # 同思路1这里
                if distance > top_1:
                    # 注意这里一定要先更新第二个距离，再更新第一个，否则顺序颠倒的话第二个距离会等于第一个距离
                    top_2 = top_1
                    top_1 = distance
                    # 或者采用这种swap的形式写，同一行更新
                    # top_1_distance, top_2_distance = distance, top_1_distance
                # 如果大于第二个，则只更新第二个距离
                elif distance > top_2:
                    top_2 = distance

        # 更新最多节点个数，这里需要最多的两个子节点 + 当前节点，所以如果就算当前节点和父节点label一样，也不再需要去父节点更新，
        # 可以直接当前节点时候就更新了全局参数，记录了最多节点的情况路径
        self.ans = max(self.ans, top_1 + top_2 + 1)

        # 返回最长的距离，要 +1 带上当前节点
        return top_1 + 1

    def longestPath(self, parent: List[int], s: str) -> int:
        """
        Time O(n)
        Space O(n)
        思路一是从edge的角度进行计算，其实这个题目要的是节点个数，我们完全可能从节点角度计算最长个数，这样只需要在当前节点时候更新最长个数即可
        不再需要在父节点计算个数。详细见注释。
        """
        graph = self.build_graph(parent)

        self.dfs(0, graph, 0, s)

        return self.ans


s1 = Solution2()
print(s1.longestPath(parent=[-1, 0, 0, 0], s="aabc"))
s2 = Solution2()
print(s2.longestPath(parent=[-1, 0, 0, 1, 1, 2], s="abacbe"))
s3 = Solution2()
print(s3.longestPath(parent=[-1, 0, 1], s="aab"))
