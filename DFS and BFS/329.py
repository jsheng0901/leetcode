from typing import List


class Solution1:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.result = 1

    def dfs(self, matrix, i, j, visited, length):
        m = len(matrix)
        n = len(matrix[0])

        visited[i][j] = True
        self.result = max(self.result, length)

        for direction in self.directions:
            next_i = i + direction[0]
            next_j = j + direction[1]
            if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                continue
            if visited[next_i][next_j]:
                continue
            if matrix[next_i][next_j] <= matrix[i][j]:
                continue
            self.dfs(matrix, next_i, next_j, visited, length + 1)

        visited[i][j] = False
        return

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Time O((m  * n)^2)
        Space O(m * n)
        DFS直接走遍所有点可能得最长path，然后全局变量记录最长path的值。前序遍历的思维方式，遇到当前点就 +1 path长度，然后更新全局变量。
        这种算法存在大量的重复计算，因为当前节点可以走的最长递增path应该可以由四个邻居方向可以走到的最长递增path +1得到。
        """
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                visited = [[False] * n for _ in range(m)]
                self.dfs(matrix, i, j, visited, 1)

        return self.result


class Solution2:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dp(self, matrix, i, j, visited, memo):
        # 遇到计算过的节点结果，直接返回，避免重复计算
        if memo[i][j] != -1:
            return memo[i][j]

        m = len(matrix)
        n = len(matrix[0])
        # 标记访问过此节点
        visited[i][j] = True
        # 记录四个方向邻居节点的返回值
        res = []
        # 遍历四个方向
        for direction in self.directions:
            next_i = i + direction[0]
            next_j = j + direction[1]
            # 越界，跳过
            if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                continue
            # 访问过，跳过
            if visited[next_i][next_j]:
                continue
            # 邻居节点不是递增，跳过
            if matrix[next_i][next_j] <= matrix[i][j]:
                continue
            # 跳入符合的邻居节点
            sub_res = self.dp(matrix, next_i, next_j, visited, memo)
            # 结果加入此层子结果
            res.append(sub_res)

        # 离开当前节点，撤销访问过，这里一定要回溯撤销，因为当前路径走过的点可能别的路径也可以走
        visited[i][j] = False
        # 此处拿到当前节点的所有子节点结果，后续遍历处理逻辑
        # 如果是空的子节点，意味走到path的底，直接返回1，同时记录进备忘录
        if len(res) == 0:
            memo[i][j] = 1
            return memo[i][j]
        # 如果有返回值，说明邻居节点右合理地递增路径，选择最大值并加上自己，同时记录进备忘录
        else:
            memo[i][j] = max(res) + 1
            return memo[i][j]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Time O(m * n)
        Space O(m * n)
        遍历一次matrix就足够了，用备忘录记录走过的结果，动态规划思想，
        当前节点可以走的最长递增path应该可以由四个邻居方向可以走到的最长递增path +1得到。我们通过后续遍历返回值，
        每次处理邻居path中的最大值 +1 即可得到当前最长path，不能用全局变量记录，后续遍历返回结果，记录进备忘录。
        """
        m = len(matrix)
        n = len(matrix[0])
        # 构建备忘录
        memo = [[-1] * n for _ in range(m)]
        # 记录最长path
        longest_path = 1

        for i in range(m):
            for j in range(n):
                # 每一次访问前初始化visited数组，因为每一次走过的路径都不一样，当前节点可走路径不受之前走过的影响
                visited = [[False] * n for _ in range(m)]
                # 得到当前节点对应的最长path，开始递归
                res = self.dp(matrix, i, j, visited, memo)
                # 更新最长path全局结果
                longest_path = max(longest_path, res)

        return longest_path


s = Solution2()
print(s.longestIncreasingPath(matrix=[[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
print(s.longestIncreasingPath(matrix=[[7, 8, 9], [9, 7, 6], [7, 2, 3]]))
print(s.longestIncreasingPath(matrix=[[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
