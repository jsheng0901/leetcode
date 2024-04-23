from typing import List


class Solution:
    def __init__(self):
        self.matchs = {}

    def dfs(self, grid, i, visited_col):
        # 问一遍每一个girl
        for j in range(len(grid[0])):
            # 如果可能是潜在的partner并且这个girl没有被问过之前
            if grid[i][j] == 1 and j not in visited_col:
                # 访问这个girl
                visited_col.add(j)
                # 如果没有partner，自动match上，如果有才会进入递归查看这个boy能不能换一个partner
                if j not in self.matchs or self.dfs(grid, self.matchs[j], visited_col):
                    # match上girl和boy
                    self.matchs[j] = i
                    # 返回 true
                    return True

        # 都不能match上，当前节点返回false
        return False

    def maximumInvitations(self, grid: List[List[int]]) -> int:
        """
        Time O(m * n)
        Space O(n)
        此题也可以用backtracking来找到所有可行的组合，然后判断edge的个数，但是会TLE。
        Hungarian算法，找出最多edge的双向图。对于每个boy，我需要去问一遍所有可能接受的girl，如果没有partner，则自动match上，
        如果有partner，则看看girl的partner能不能换一个partner，如果可以换成功，则匹配现在的boy。详细见注释
        """
        # 遍历每个boy，也就是每一行
        for i in range(len(grid)):
            # 每次初始化访问过的girl，保证不能走回头路
            self.dfs(grid, i, set())

        return len(self.matchs)


s = Solution()
print(s.maximumInvitations(grid=[[1, 0, 1, 0],
                                 [1, 0, 0, 0],
                                 [0, 0, 1, 0],
                                 [1, 1, 1, 0]]))
