from typing import List, Union, Any


class Solution1:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Time O(n * m)
        Space O(n * m)
        dp[i][j]记录从左上角走到[i][j]需要的最小路劲和。dp[i][j]从dp[i - 1][j]和dp[i][j - 1]得到，所以我们从上到下从左到右遍历dp数组。
        初始化第一行和第一列和第一个左上角点。详细见注释。
        """
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        # 初始化左上角为grid初始值
        dp[0][0] = grid[0][0]

        # 初始化第一列
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # 初始化第一行
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                # 状态转移，由左和上得到
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        # 返回结果
        return dp[-1][-1]


class Solution2:
    def __init__(self):
        self.memo = None

    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Time O(n * m)
        Space O(n * m)
        同思路1，只是换成自底向上的写法，此题还以直接用最短路径的graph的算法，只是这里可以用DP是因为只能走两个方向并且不能走回头路的图。
        """
        m = len(grid)
        n = len(grid[0])
        # 构造备忘录，初始值全部设为 -1
        self.memo = [[-1 for _ in range(n)] for _ in range(m)]

        return self.dp(grid, m - 1, n - 1)

    def dp(self, grid: List[List[int]], i: int, j: int) -> Union[Union[int, float], Any]:
        # 走到底了，直接返回结果
        if i == 0 and j == 0:
            return grid[0][0]

        # 越界，返回极大值
        if i < 0 or j < 0:
            return float('inf')

        # 避免重复计算
        if self.memo[i][j] != -1:
            return self.memo[i][j]

        # 将计算结果记入备忘录
        self.memo[i][j] = min(
            self.dp(grid, i - 1, j),
            self.dp(grid, i, j - 1)
        ) + grid[i][j]

        return self.memo[i][j]


s = Solution2()
print(s.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
