class Solution:
    def dp(self, n, num_absent, num_late, mod, memo):
        # 不符合题意，此path不能再继续走下去，返回0
        if num_absent >= 2 or num_late >= 3:
            return 0

        # 找到一条合理的path
        if n == 0:
            return 1

        # 记忆化搜索存在
        if memo[n][num_absent][num_late] != -1:
            return memo[n][num_absent][num_late]

        # 统计子节点返回个数
        sub = 0
        # 遍历三种情况
        for letter in ['A', 'L', 'P']:
            # 如果是absent，对应的absent次数 +1
            if letter == 'A':
                sub += self.dp(n - 1, num_absent + 1, 0, mod, memo) % mod
            # 如果是late，对应连续的late次数 +1
            elif letter == 'L':
                sub += self.dp(n - 1, num_absent, num_late + 1, mod, memo) % mod
            # 如果是present，无变化
            else:
                sub += self.dp(n - 1, num_absent, 0, mod, memo) % mod

        # 记录进备忘录
        memo[n][num_absent][num_late] = sub % mod

        return memo[n][num_absent][num_late]

    def checkRecord(self, n: int) -> int:
        """
        Time O(n * 3 * 2) -> O(6n) -> O(n)
        Space O(n)
        三种状态，分别是长度，absent的次数，和连续late的次数。构建三维DP备忘录，后续遍历DFS带备忘录写法。详细见注释。
        """
        mod = 10 ** 9 + 7
        # 构建备忘录
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]
        # 统计所有可能的path个数
        total_records = self.dp(n, 0, 0, mod, memo)

        return total_records


s = Solution()
print(s.checkRecord(n=1))
print(s.checkRecord(n=2))
