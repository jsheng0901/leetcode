class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Time O(n^2)
        Space O(n^2)
        动态规划，dp定义为为字符串s在[i, j]范围内最长的回文子序列的长度为dp[i][j]
        如果s[i]与s[j]相同，那么dp[i][j] = dp[i + 1][j - 1] + 2，因为i, j一定在回文中，需要同时缩小看i+1和j-1的情况。
        如果s[i]与s[j]不相同，说明s[i]和s[j]的同时加入 并不能增加[i,j]区间回文子序列的长度，
        那么分别加入s[i]，s[j]看看哪一个可以组成最长的回文子序列。加入s[j]的回文子序列长度为dp[i + 1][j]。
        加入s[i]的回文子序列长度为dp[i][j - 1]。
        """

        dp = [[0] * len(s) for _ in range(len(s))]
        # 当i与j相同，那么dp[i][j]一定是等于1的，即：一个字符的回文子序列长度就是1。
        for i in range(len(s)):
            dp[i][i] = 1

        # 从递归公式中，可以看出，dp[i][j] 依赖于 dp[i + 1][j - 1] ，dp[i + 1][j] 和 dp[i][j - 1]
        # 遍历i的时候一定要从下到上遍历，j的话，可以正常从左向右遍历。
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                # 相等的情况
                if s[i] == s[j]:
                    # 对应情况1
                    dp[i][j] = dp[i + 1][j - 1] + 2
                # 不相等的情况
                else:
                    # 对应情况2
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # 这里的返回值需要注意的不是[-1][-1]，因为dp的含义是 i --> j 的回文长度，所以取左右两端，及i = 0，j = len(s) - 1 或者数组 -1
        return dp[0][-1]
