class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """动态规划，dp为字符串s在[i, j]范围内最长的回文子序列的长度为dp[i][j]"""
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:            # 相等的情况
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])      # 不相等的情况
        return dp[0][-1]
