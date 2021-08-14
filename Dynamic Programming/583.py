class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """dp找最长公共子序列的长度，再用总长度减去两边的最长公共长度"""
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return len(word1) + len(word2) - dp[i][j] * 2


s = Solution()
print(s.minDistance(word1="leetcode", word2="etco"))
