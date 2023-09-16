class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Time O(n * m)
        Space O(n * m)
        dp[i][j] 表示以下标i-1为结尾的字符串word1，和以下标j-1为结尾的字符串word2，最近编辑距离为dp[i][j]。
        四种情况来增删替换或者不动。见注释。
        """
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # dp[i][0] ：以下标i-1为结尾的字符串word1，和空字符串word2，最近编辑距离为dp[i][0]。
        # 那么dp[i][0]就应该是i，对word1里的元素全部做删除操作，即：dp[i][0] = i;
        for i in range(len(word1) + 1):
            dp[i][0] = i
        # 同i的初始化一样
        for j in range(len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                # 如果此时字符相等，那么说明不用任何编辑
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # 如果不相等
                else:
                    # 操作一：word1删除一个元素，那么就是以下标i - 2为结尾的word1 与 j-1为结尾的word2的最近编辑距离 再加上一个操作。
                    # 操作二：word2删除一个元素，那么就是以下标i - 1为结尾的word1 与 j-2为结尾的word2的最近编辑距离 再加上一个操作。
                    # 操作三：替换元素，word1替换word1[i - 1]，使其与word2[j - 1]相同，此时不用增删加元素。
                    # 回到成上一个[i - 1][j - 1]，也就是上一个字符相等的情况下，只需要增加一次替换的操作。
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[-1][-1]
