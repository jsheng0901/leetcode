from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.result = 0

    def dfs(self, node, edges_dict, hasApple, visited):

        # 进入递归的所有节点都是valid过的，所以不需要递归终止判断，直接记录visited
        visited[node] = True
        # 记录所有子节点的edge是否需要
        child_res = []

        # 遍历所有子节点
        for nei in edges_dict[node]:
            # 判断子节点存在并且没有访问过，因为是无向图！！！
            if nei and visited[nei] is False:
                res = self.dfs(nei, edges_dict, hasApple, visited)
                # 如果子节点需要访问，则result +1
                if res:
                    self.result += 1
                # 记录子节点情况
                child_res.append(res)

        # 第一种情况当前节点任意一个子节点需要访问，则当前节点edge都需要访问，返回True
        if any(child_res):
            return True
        else:
            # 第二种情况，当前节点任意一个子节点都不需要访问，当前节点包含Apple则edge需要访问，返回True
            if hasApple[node]:
                return True
            # 第三种情况，子节点和当前节点都不需要访问
            else:
                return False

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        Time O(n)
        Space O(n)
        此题虽然是树的描述，但是其实和树没啥关系，相信成graph更好理解。
        首先构建edges字典需要同时记录双向的关系，敲重点：因为题目是无向图！！！！同时用visited数组记录是否访问过来避免重复访问节点。
        DFS的思路+后序遍历的思路，每次在所有邻居节点也就是子节点处理完之后再处理当前节点，三种情况对于当前节点：
        1. 子节点需要访问当前节点不包含Apple：
            此时当前节点的edge也需要记录，因为子节点需要访问。
        2. 子节点不需要访问但当前节点包含Apple：
            此时当前节点的edge也需要记录，因为当前节点包含Apple。
        3. 子节点和当前节点都不需要访问
        需要记录则返回True，然后再loop递归结束后判断每个edge情况，如果True则result +1
        """
        edges_dict = defaultdict(list)
        for edge in edges:
            edges_dict[edge[0]].append(edge[1])
            edges_dict[edge[1]].append(edge[0])

        visited = [False] * n

        self.dfs(0, edges_dict, hasApple, visited)

        return self.result * 2


s1 = Solution()
s2 = Solution()
s3 = Solution()
s4 = Solution()
print(s1.minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                 hasApple=[False, False, True, False, True, True, False]))
print(s2.minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                 hasApple=[False, False, True, False, False, True, False]))
print(s3.minTime(n=4, edges=[[0, 1], [1, 2], [0, 3]],
                 hasApple=[True, True, True, True]))
print(s4.minTime(n=4, edges=[[0, 2], [0, 3], [1, 2]],
                 hasApple=[False, True, False, False]))
