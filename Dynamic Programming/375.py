class Solution1:
    def dfs(self, left, right):
        # 走到底了，直接返回0，因为不需要再猜了
        if left >= right:
            return 0

        # 子节点的所有情况下的最小值
        sub_min = float('inf')

        # 遍历所有子节点中每个点作为pivot的情况
        for i in range(left, right + 1):
            # 左右节点的结果
            left_res = self.dfs(left, i - 1)
            right_res = self.dfs(i + 1, right)
            # 得到当前节点作为pivot节点的cost
            sub = i + max(left_res, right_res)
            # 更新子节点结果
            sub_min = min(sub_min, sub)

        return sub_min

    def getMoneyAmount(self, n: int) -> int:
        """
        Time O(n!)
        Space O(n)
        此题的状态转移公式为 cost(1, n) = i + max(cost(1, i−1), cost(i + 1, n))
        对每个点作为pivot的情况进行搜索，得到左右两边的最大值的，所有可能性中的最小值的结果。后续遍历返回最值。
        但是明显TLE，因为需要遍历次数太多了。
        """
        return self.dfs(1, n)


class Solution2:
    def dfs(self, left, right):
        if left >= right:
            return 0

        sub_min = float('inf')
        # 优化在这里，搜索区间减半
        for i in range(int((left + right) / 2), right + 1):
            left_res = self.dfs(left, i - 1)
            right_res = self.dfs(i + 1, right)
            sub = i + max(left_res, right_res)
            sub_min = min(sub_min, sub)

        return sub_min

    def getMoneyAmount(self, n: int) -> int:
        """
        Time O(n!)
        Space O(n)
        同思路1，但是我们每次左右遍历的时候，如果左边比右边长度小，那么最大值的情况一定在右边，所以我们并不需要遍历所有节点作为pivot的情况，
        只需要在到当前区间内一半的搜索区间即可。不过还是有很多重复自区间的搜索。还是会TLE
        """
        return self.dfs(1, n)


class Solution3:
    def dp(self, left, right, memo):
        if left >= right:
            return 0

        # 备忘录，记忆化返回搜索过的结果
        if memo[left][right] != 0:
            return memo[left][right]

        sub_min = float('inf')

        for i in range((left + right) // 2, right + 1):
            left_res = self.dp(left, i - 1, memo)
            right_res = self.dp(i + 1, right, memo)
            sub = i + max(left_res, right_res)
            sub_min = min(sub_min, sub)

        # 存储当前节点遍历的区间得到的结果
        memo[left][right] = sub_min

        return memo[left][right]

    def getMoneyAmount(self, n: int) -> int:
        """
        Time O(n^2)
        Space O(n^2)
        此题明显有重复子区间的搜索，需要带备忘录的DFS也就是DP的思路来进行记忆化搜索达到，降低时间复杂度到搜索空间只有O(n^2)。
        """
        # memo[i][j] 表示在 [i, j] 区间内最小值是多少
        memo = [[0] * (n + 1) for _ in range(n + 1)]

        return self.dp(1, n, memo)


s = Solution3()
print(s.getMoneyAmount(n=10))
print(s.getMoneyAmount(n=1))
print(s.getMoneyAmount(n=2))
