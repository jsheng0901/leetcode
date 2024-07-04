from typing import List


class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
        self.res = 0

    def backtracking(self, grid, i, j, gold):

        m, n = len(grid), len(grid[0])
        # 存储原本的值
        original_gold = grid[i][j]
        # 记录走到当前节点总共多少gold
        gold += original_gold
        # 设置为0，防止走回头路
        grid[i][j] = 0
        # 更新最大gold值
        self.res = max(self.res, gold)
        # 遍历四个方向
        for direction in self.directions:
            next_i = i + direction[0]
            next_j = j + direction[1]
            # 越界，跳过
            if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                continue
            # 等于0，访问过或者是空cell，跳过
            if grid[next_i][next_j] == 0:
                continue
            # 继续回溯剩下三个方向
            self.backtracking(grid, next_i, next_j, gold)
        # 离开当前节点的时候回溯一下，其实Python用的是当前递归函数的输入值作为gold，也就是说上一层的gold不会受当前节点影响，
        # 所以是否回溯这里不重要，其实也可以不需要回溯
        gold -= original_gold
        # 但是标记grid的mutable的list，一定要回溯，不然上一层的grid会受到这一层的影响
        grid[i][j] = original_gold

        return

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        """
        Time O(m * n - g + g * 3^g)     g --> number of gold cell
        Space O(g)
        遍历所有cell，对于每个gold cell我们找到所有可能的path，时刻更新最大值的path。这里对于每个gold cell我们会遍历3个方向，
        所以在递归方程loop里面有g * 3^g。空间复杂度取决于递归栈的个数也就是gold cell个数。详细见注释。这里为了防止走回头路，把访问过的cell
        标记为0，这样就会不重复访问，离开节点时候记得把cell设置回原来的值。
        """
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                # 遍历所有gold cell
                if grid[i][j] != 0:
                    self.backtracking(grid, i, j, 0)

        return self.res


s = Solution()
print(s.getMaximumGold(grid = [[0,6,0],[5,8,7],[0,9,0]]))
print(s.getMaximumGold(grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))

