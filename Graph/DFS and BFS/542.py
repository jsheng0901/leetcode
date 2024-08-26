from typing import List


class Solution:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(self, mat, visited, result):
        m = len(mat)
        n = len(mat[0])

        # 初始化队列
        queue = []
        # 把那些值为 0 的坐标放到队列里，同时标记访问过同时更新结果，这里体现逻辑，更不更新无所谓，因为初始化都是0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = True
                    result[i][j] = 0

        # 执行 BFS 算法框架，从值为 0 的坐标开始向四周扩散，这里有个巧妙的地方是，没有访问过的一定都是1，因为0都已经访问过了在上面
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.pop(0)
                # 向四周扩散
                for direction in self.directions:
                    next_i = i + direction[0]
                    next_j = j + direction[1]
                    # 越界，则跳过
                    if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                        continue
                    # 访问过说明要么是0要么是访问过的1，跳过
                    if visited[next_i][next_j] is True:
                        continue
                    # 到这里一定是没有越界并且没访问过的点
                    # 加入列队，同时标记访问过，更新结果数组，用DP的思想，到此没有访问过的点的最小距离等于前一个访问过的点的最小距离 +1
                    queue.append((next_i, next_j))
                    visited[next_i][next_j] = True
                    result[next_i][next_j] = result[i][j] + 1

        # 结束列队，返回结果
        return result

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Time O(n * m)
        Space O(n * m)
        核心思想是下一步到0的最短距离等于邻居到0的最短距离再 +1。动态规划思想 + BFS写法找出最短路径。
        这里也可以不需要visited数组来记录是否访问过，在result里面初始化 -1，如果访问过就标记最短距离，没有访问过则刚好是 -1。
        """
        m = len(mat)
        n = len(mat[0])

        # 记录答案的结果数组
        result = [[0] * n for _ in range(m)]
        # 记录是否访问过
        visited = [[False] * n for _ in range(m)]

        return self.bfs(mat, visited, result)


s = Solution()
print(s.updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
print(s.updateMatrix(
    mat=[[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
         [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]))

