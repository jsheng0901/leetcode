class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        Time O(n * m)
        Space O(n * m)
        同1143和583，区别在于，这里dp[i][j]的含义是以s1[i-1]，s2[j-1]结尾的字符最长的公共子序列的最大ASCII值。
        其实就是我们每次存储的不是长度而是此时最长子序列对应的同时最大的ASCII值。
        """
        # 遍历两个字符，存储原始的ASCII值和
        s1_value = 0
        s2_value = 0
        for i in range(len(s1)):
            s1_value += ord(s1[i])

        for j in range(len(s2)):
            s2_value += ord(s2[j])

        # 构建dp，此处原理同最长子序列
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                # 两个字符相等
                if s1[i - 1] == s2[j - 1]:
                    # 存储字符对应的ASCII值
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
                else:
                    # 不相等，取最大的ASCII值
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        max_common_substring_value = dp[-1][-1]

        # 利用总和减去最大相等部分，得出最小删除部分
        min_delete_sum = s1_value + s2_value - 2 * max_common_substring_value

        return min_delete_sum


s = Solution()
print(s.minimumDeleteSum(s1="delete", s2="leet"))
