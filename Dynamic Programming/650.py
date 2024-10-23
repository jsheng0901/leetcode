class Solution1:
    def dp(self, n, cur, paste_len, memo):
        # 超过长度，直接返回无穷
        if cur > n:
            return float('inf')
        # 找到一条合理的path
        if cur == n:
            return 0

        # 备忘录直接返回结果
        if memo[cur][paste_len] != -1:
            return memo[cur][paste_len]

        sub = float('inf')

        # 第一条路，执行copy paste 一起，注意这里可以一起执行
        sub = min(sub, self.dp(n, cur * 2, cur, memo) + 2)
        # 第二条路，只执行paste
        sub = min(sub, self.dp(n, cur + paste_len, paste_len, memo) + 1)

        # 写进备忘录
        memo[cur][paste_len] = sub

        return sub

    def minSteps(self, n: int) -> int:
        """
        Time O(n^2)
        Space O(n^2)
        标准的自顶向下的DP写法，每次考虑两条路，最终返回最短路径，注意这里返回路径类似找树的深度，走到终点后直接返回0，
        然后每一次递归叠加一步返回。
        """
        # 特殊情况
        if n == 1:
            return 0
        # 构建备忘录
        memo = [[-1] * (n // 2 + 1) for _ in range(n + 1)]

        # 注意这里要先执行一次copy操作，不然会陷入无限copy的死循环
        return self.dp(n, 1, 1, memo) + 1


class Solution2:
    def minSteps(self, n: int) -> int:
        """
        Time O(n^2)
        Space O(n)
        DP的思路，自底向上写法。这里有个优化的思路就是，一个数如果可以被他的因子j整除，那么一定可以通过叠加除数的次数来实现这个数
        """
        dp = [1000] * (n + 1)

        # Base case
        dp[1] = 0
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                # Copy All and Paste (i-j) / j times
                # for all valid j's
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)

        return dp[n]


class Solution3:
    def minSteps(self, n: int) -> int:
        """
        Time O(sqrt(n))
        Space O(1)
        数学原理，参考：https://leetcode.com/problems/2-keys-keyboard/submissions/1429726903/
        """
        ans = 0
        d = 2
        while n > 1:
            # If d is prime factor, keep dividing
            # n by d until is no longer divisible
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        return ans


s = Solution2()
print(s.minSteps(n=3))
