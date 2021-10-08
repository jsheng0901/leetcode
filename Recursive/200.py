class Solution:
    def dfs(self, grid, i, j):
        # 当超出棋盘范围，或者是0的时候则停止
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] != '1':
            return

        grid[i][j] = '0'
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)

        return

    def numIslands(self, grid: [[str]]) -> int:
        """
        此题目的是找到连续为1的路径有几种，所以一直递归到四周都不是1的时候，停止递归，此时count += 1

        递归思路，每次判断当前是不是1，如果不是则跳过，
        是1则判断旁边四个是不是1，每次路过1的时候，改成0，防止loop重复的节点
        """
        if len(grid) == 0:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1

        return count
