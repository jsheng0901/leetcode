class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        和最长连续公共子序列不同的地方在于不用连续, 对于当两个text不同的时候也要记录当前最长的子序列长度
        :param text1:
        :param text2:
        :return:
        """
        dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


s = Solution()
print(s.longestCommonSubsequence(text1="abcde", text2="ace"))
