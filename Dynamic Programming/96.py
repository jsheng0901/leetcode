class Solution:
    def numTrees(self, n: int) -> int:
        # time O(n^2), space O(n)
        # dp[i] ：1到i为节点组成的二叉搜索树的个数为dp[i]。
        dp = [0] * (n + 1)

        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                # 找到当前节点数和之前节点数的关系
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[-1]


s = Solution()
print(s.numTrees(n=5))
