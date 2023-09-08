class Solution:
    def minCut(self, s: str) -> int:
        """
        Time O(n^2)
        Space O(n^2)
        dp[i]：范围是[0, i]的回文子串，最少分割次数是dp[i]。
        递推公式：当切割点j在[0, i] 之间时候，dp[i] = dp[j] + 1，因为要找最少在loop的时候，所以要加min
        初始化：dp[0]一定是0，长度为1的字符串最小分割次数就是0
        is_palindrome来源于5/647题目，目的在于判断[i, j]区间是否是回文。
        """
        # 构建二维数组来记录is_palindrome[i][j]代表区间[i, j]是否是回文
        is_palindrome = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        is_palindrome[i][j] = True
                    elif is_palindrome[i + 1][j - 1]:
                        is_palindrome[i][j] = True

        dp = [len(s)] * len(s)
        dp[0] = 0

        for i in range(1, len(s)):
            # 如果[0, i]是回文，则不需要切割，直接赋值0并且进入下一个字符
            if is_palindrome[0][i]:
                dp[i] = 0
                continue
            # 如果不是回文，从0 -> i开始循环判断如何切割最少，并且保证都是回文
            for j in range(i):
                # 如果找到[j+1, i]是回文，则说明多一个切断点，+1。
                if is_palindrome[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]


s = Solution()
print(s.minCut(s="aabc"))
