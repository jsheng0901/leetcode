class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Time O(n * m)
        Space O(n * m)
        思路：dp先找到最长公共子序列的长度，再用总长度减去两边的最长公共长度。
        dp[i][j]：以i-1为结尾的word1子序列中以j-1为结尾的word2子序列中最长公共子序列的个数dp[i][j]，总共两种情况，见注释。
        """
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                # 当字符相等的时候，及找到上一个字符的情况 +1
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 不相等的时候，可以删除word1或者删除word2当前字符达到子序列相等，取两者中最大值。
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        max_common_string_length = dp[-1][-1]

        step_to_delete = len(word1) + len(word2) - 2 * max_common_string_length

        return step_to_delete


s = Solution()
print(s.minDistance(word1="leetcode", word2="etco"))
