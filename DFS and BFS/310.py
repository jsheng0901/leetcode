from collections import defaultdict
from typing import List


class Solution1:
    def bfs(self, graph, root, n):
        queue = []
        visited = [False] * n
        height = 0

        queue.append(root)
        visited[root] = True

        while queue:
            size = len(queue)
            for i in range(size):
                top = queue.pop(0)
                for nei in graph[top]:
                    if visited[nei] is False:
                        queue.append(nei)
                        visited[nei] = True
            height += 1

        return height

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Time O(n * edges)   每个点都要走一遍整个图
        Space O(n)
        每个点都可能是root，所以直接loop所有点是root的情况，每次loop走完整个graph，算出最长距离及bfs的step。
        然后对比最短的step，并记录下来相对的root。此方法会超时当graph特别大的时候。
        """
        graph = defaultdict(list)
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)

        min_height = float('inf')
        result = []
        for node_id in range(n):
            height = self.bfs(graph, node_id, n)
            if height < min_height:
                min_height = height
                result = [node_id]
            elif height == min_height:
                result.append(node_id)

        return result


class Solution2:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Time O(edges)   走一遍所有结点即可
        Space O(n)      存储叶子结点
        反向思维，不从root遍历，从叶子节点遍历，一层一层地删除叶子节点（每删除一层叶子节点，就会产生新的叶子节点），
        直到剩下的节点数小于等于2个为止。之所以是2个而不是1个，是因为如果输入的这幅图两边完全对称，可能出现两个节点都可以作为根节点的情况。
        此时最后剩下的叶子节点就是我们可能的根节点。
        核心想法：找最近叶子节点就从根开始 BFS，找根节点的话就从叶子开始 BFS
        """
        # 特殊情况
        if len(edges) == 0:
            return [0]

        # 构建双向及无向图
        graph = defaultdict(list)
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)

        # 找到所有的最开始的叶子节点
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        remain_node_number = n
        # 不断删除叶子节点，直到剩下的节点数小于等于 2 个
        while remain_node_number > 2:
            # 删除当前叶子节点，计算新的叶子节点
            remain_node_number -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                # 将被删除的叶子节点的邻接节点的度减 1，及移除邻居节点和叶子节点的链接关系，此出之前取 index 0 因为叶子节点就一条边
                nei = graph[leaf][0]
                graph[nei].remove(leaf)
                # 如果邻接节点的度为 1，说明它也变成了叶子节点
                if len(graph[nei]) == 1:
                    # 加入进新的叶子节点栈
                    new_leaves.append(nei)
            # 更新叶子节点栈
            leaves = new_leaves

        # 最后剩下的节点就是根节点
        return leaves


s = Solution2()
print(s.findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]))
