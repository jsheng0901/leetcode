class Solution:
    def minInsertions(self, s: str) -> int:
        """
        Time O(n^2)
        Space O(n^2)
        动态规划，此题等价于先找到原来s里面最长的回文子序列，然后剩下不是回文的就是我们需要至少insert的新的字符。前面的部分同516。
        dp定义为为字符串s在[i, j]范围内最长的回文子序列的长度为dp[i][j]，此部分详细解释见516。
        """

        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        # 同516到这里位置，都是找最长回文子序列
        # 返回总体长度减最长就是我们要增加的字符长度
        return len(s) - dp[0][-1]


s = Solution()
print(s.minInsertions(s="leetcode"))
