from collections import defaultdict
from typing import List


class Solution1:
    def __init__(self):
        self.total_path = 0

    def dfs(self, graph, visited, node, cur_path):
        # 标记访问过
        visited[node] = True
        # 记录总路径和 = 每次到一个点的当前路径和从根节点到当前节点
        self.total_path += cur_path
        # 遍历邻居节点
        for nei in graph[node]:
            # 访问过则跳过
            if visited[nei] is True:
                continue
            # 继续邻居节点递归，同时路径长度 +1
            self.dfs(graph, visited, nei, cur_path + 1)

        return

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Time O(n^2)
        Space O(n)
        遍历每个点，每个点都走一遍DFS的前序遍历思路，每次走到一个点就说明path +1，同时全局记录总路径 +path。
        此方法会超时，很不高效，因为走过很多重复的路径。
        """
        # 构建无向图
        graph = defaultdict(list)
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)

        res = []
        for i in range(n):
            # 每一次初始化visited数组记录不走回头路
            visited = [False] * n
            # 每次初始化一个点到其它点的总路径全局变量
            self.total_path = 0
            # 开始递归
            self.dfs(graph, visited, i, 0)
            # 加入结果
            res.append(self.total_path)

        return res


class Solution2:

    def postorder(self, graph, cur, pre, dis, num_node):
        # 当前节点自己也是一个节点
        num_node[cur] += 1
        # 遍历邻居节点
        for nei in graph[cur]:
            # 因为是树的结构在图里面，所有用pre指针表示父节点
            # 因为这里树的遍历不能走回头路，所有如果是父节点则跳过
            if nei == pre:
                continue
            # 后续遍历
            self.postorder(graph, nei, cur, dis, num_node)
            # 当前节点为根的子树节点个数
            num_node[cur] += num_node[nei]
            # 当前节点到底的路径和 = 邻居节点到底的路径和 + 有几个邻居节点的子节点
            dis[cur] += dis[nei] + num_node[nei]

        return

    def preorder(self, graph, cur, pre, n, dis, num_node):
        # 前序遍历0为根节点的树
        for nei in graph[cur]:
            # 同后续遍历，不能走回头路
            if nei == pre:
                continue
            # 动态规划思路，状态转移方程
            # dis[cur]现在是正确的，和cur链接的点到cur的距离要 -1
            # 则以nei为root的子树中所有节点都需要距离 -1
            # 所以dis[nei] = dis[cur] - 1 * num_node[nei]
            # 但同时以nei为root的子树之外的其它节点到cur的距离要 +1
            # 这里省去了 * 1 这个操作
            dis[nei] = dis[cur] - num_node[nei] + n - num_node[nei]
            self.preorder(graph, nei, cur, n, dis, num_node)

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        dp + 树的遍历思想，构建两个数组，num_node[i]表示以0为根节点的树，节点i的子节点有多少个，dis[i]表示节点i到其它节点的路径总和。
        我们先后序遍历，记录0为根的树，每个节点的子节点个数。同时记录0为根节点时每个当前节点走到底的路径总和。之后在前序遍历更新dis数组结果。
        这里dp的核心思路是dp[1] = dp[0] - 1 * num_node[1] + (n - num_node[1]) * 1
        邻居节点到其它节点路径和 = 当前节点 - 当前节点子节点个数 + 除去当前节点的子节点个数。
        """
        # 构件图
        graph = defaultdict(list)
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)

        # 初始化两个数组
        num_node = [0] * n
        dis = [0] * n

        # 开始后续和前序递归
        self.postorder(graph, 0, -1, dis, num_node)
        self.preorder(graph, 0, -1, n, dis, num_node)

        return dis


s = Solution2()
print(s.sumOfDistancesInTree(n=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
