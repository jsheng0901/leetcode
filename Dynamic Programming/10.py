class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Time O(m * n)
        Space O(m * n)
        定义：dp[i][j]表示从字符串到s[i - 1]与到p[j - 1]的匹配情况。
        """
        m = len(s)
        n = len(p)

        # 初始化都为 false，这里初始化 +1 因为dp里面的第0行和第0列理解为空字符串，1开始才是真正的字符串s和p
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # 初始化为true，因为空字符肯定可以匹配空字符
        dp[0][0] = True

        # 需要对空字符串和p特殊赋值
        for j in range(1, n + 1):
            # 当p是 * 的时候，空字符可以匹配 ex: a* 但不能匹配 aa*
            # 比如 j = 2，p = a* 可以匹配 s = ''
            # 比如 j = 3，p = aa* 不可以匹配 s = ''
            # 这里不会出现p = * 的情况，因为是不合理的pattern，题目保证了不会出现
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 对应的当前字符相等或者 p 等于 '.'，此时检查前一个字符串情况
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                # 如果当前不相等，并且 p 等于 *，这里也不会出现 p = * 的情况，因为不合理，等价于题目保证了 j >= 2 在这里
                elif p[j - 1] == '*':
                    # 如果当前*前的字母没有匹配上并且也不是 '.'，说明说明 * 匹配的是0次
                    if s[i - 1] != p[j - 2] and p[j - 2] != '.':
                        # 需要注意的是这里 -2 因为，当前是 * 的时候的前一个不匹配，则说明要看 * 的前两个的状态，及dp里面j对应的j - 2
                        dp[i][j] = dp[i][j - 2]
                    # 如果匹配上了就判断匹配的是一次还是多次的状态
                    else:
                        # dp[i][j - 2]为匹配上0次
                        # dp[i - 1][j]为匹配上1次或者多次
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]

        return dp[m][n]


s = Solution()
print(s.isMatch(s="aa", p="a"))
print(s.isMatch(s="aa", p="a*"))
print(s.isMatch(s="aaa", p="ab*a*c*a"))
