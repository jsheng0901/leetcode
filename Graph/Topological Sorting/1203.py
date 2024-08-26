import collections
from typing import List


class Solution:
    def build_graph(self, n, group, group_id, beforeItems):
        # Sort all item regardless of group dependencies.
        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n

        # Sort all groups regardless of item dependencies.
        group_graph = [[] for _ in range(group_id)]
        group_indegree = [0] * group_id

        for curr in range(n):
            for prev in beforeItems[curr]:
                # Each (prev -> curr) represents an edge in the item graph.
                item_graph[prev].append(curr)
                item_indegree[curr] += 1

                # If they belong to different groups, add an edge in the group graph.
                if group[curr] != group[prev]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

        return group_graph, group_indegree, item_graph, item_indegree

    def bfs(self, graph, in_degree):
        # 根据入度初始化队列中的节点
        q = []
        # add init nodes inside queue
        for i in range(len(in_degree)):
            # for empty node will also be added into init queue, since no in_degree
            if in_degree[i] == 0:
                q.append(i)

        topological_sort = []
        # 开始执行 BFS 算法
        while q:
            cur = q.pop(0)
            # 弹出节点的顺序即为拓扑排序结果
            topological_sort.append(cur)
            for nei in graph[cur]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return topological_sort if len(topological_sort) == len(graph) else []

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        """
        Time O(n^2 + (v + e))   build graph take O(n^2), topological sort take O(v + e)
        Space O(n)
        此题核心难度在于如何找到基于group的顺序，其实我们可以把group想象成一个大的节点，所以找到group的顺序也就是和找到点的顺序一样，用拓扑
        排序对整个大的group节点进行排序，同时也需要构建独立的基于group的图。详细见注释
        """
        # If an item belongs to zero group, assign it a unique group id.
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        # build two graphs
        group_graph, group_indegree, item_graph, item_indegree = self.build_graph(n, group, group_id, beforeItems)

        # topological sort on both graph
        item_order = self.bfs(item_graph, item_indegree)
        group_order = self.bfs(group_graph, group_indegree)

        # if there is cycle then can't build sorted list, return empty list
        if not item_order or not group_order:
            return []

        # Items are sorted regardless of groups, we need to
        # differentiate them by the groups they belong to.
        ordered_groups = collections.defaultdict(list)
        for item in item_order:
            ordered_groups[group[item]].append(item)

        # Concatenate sorted items in all sorted groups.
        # [group 1, group 2, ... ] -> [(item 1, item 2, ...), (item 1, item 2, ...), ...]
        answer = []
        # empty group will also be considered since in degree will be 0
        for group_index in group_order:
            answer += ordered_groups[group_index]
        return answer


s = Solution()
print(s.sortItems(n=8, m=2, group=[-1, -1, 1, 0, 0, 1, 0, -1], beforeItems=[[], [6], [5], [6], [3, 6], [], [], []]))
print(s.sortItems(n=8, m=2, group=[-1, -1, 1, 0, 0, 1, 0, -1], beforeItems=[[], [6], [5], [6], [3], [], [4], []]))
