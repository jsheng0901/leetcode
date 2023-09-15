class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        Time O(n * m)
        Space O(n * m)
        dp[i][j]：以i-1为结尾的s子序列中出现以j-1为结尾的t的个数为dp[i][j]
        状态转移公式：
        当s[i - 1] 与 t[j - 1]相等时，dp[i][j]可以有两部分组成。
        一部分是用s[i - 1]来匹配，那么个数为dp[i - 1][j - 1]。即不需要考虑当前s子串和t子串的最后一位字母，所以只需要 dp[i-1][j-1]。
        一部分是不用s[i - 1]来匹配，个数为dp[i - 1][j]。及dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
        当s[i - 1] 与 t[j - 1]不相等时，dp[i][j]只有一部分组成，不用s[i - 1]来匹配（就是模拟在s中删除这个元素），即：dp[i - 1][j]
        所以递推公式为：dp[i][j] = dp[i - 1][j];
        """
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        # 初始化当t为空string的时候，s可以删除所有元素满足t，及初始值都是1
        for i in range(len(dp)):
            dp[i][0] = 1

        # 初始化当s为空string时候，无论如何都满足不了t，及初始值都是0，此处和dp初始化重叠了，可以不用写，只是凸显初始化逻辑。
        # for j in range(1, len(t) + 1):
        #     dp[0][j] = 0

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                # 相等
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                # 不相等
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]


s = Solution()
print(s.numDistinct(s="rabbbit", t="rabbit"))
