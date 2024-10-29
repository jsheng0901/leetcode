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


class Solution2:
    def dp(self, s, i, p, j, memo):
        m, n = len(s), len(p)
        # 如果pattern走到底了
        if j == n:
            # 判断一下是否string也到底了，都到底了说明是valid的，返回true，否则false
            return i == m
        # 如果string到底了
        if i == m:
            # 如果剩下的pattern长度是奇数，说明不可能是匹配0个字符的case比如 'a*a'，肯定不合理，返回false
            if (n - j) % 2 == 1:
                return False
            # 如果是偶数，判断一下剩下的是不是有字符加*的组合，比如 'a*'，如果不是的话，说明不是匹配0个字符情况，直接返回false
            for k in range(j + 1, n, 2):
                if p[k] != "*":
                    return False
            # 如果都不是上述情况，直接返回true
            return True

        # 查备忘录，防止重复计算
        if memo[i][j] != -1:
            return memo[i][j]

        # 当前后续遍历的返回结果
        res = False
        # 如果当前相等或者是 '.' 的情况，匹配
        if s[i] == p[j] or p[j] == ".":
            # case 1: p[j + 1] 为 * 通配符时
            if j < n - 1 and p[j + 1] == "*":
                # 1. p[j] 有可能会匹配多个字符，比如 s = "aaa", p = "a*"，对应 i + 1，p不动
                # 2. p[i] 也有可能匹配 0 个字符，比如 s = "aa", p = "a*aa"，对应 i不动，j + 2
                res = self.dp(s, i, p, j + 2, memo) or self.dp(s, i + 1, p, j, memo)
            # case 2: p[j + 1] 不是 * 通配符时，直接判断下一个字符
            else:
                res = self.dp(s, i + 1, p, j + 1, memo)
        # 如果 s[i] != p[j]
        else:
            # case 1: 有 * 通配符
            if j < n - 1 and p[j + 1] == "*":
                # p[j] 只能匹配 0 次，然后看下一个字符是否能和 s[i] 匹配。比如说 s = "aa", p = "b*aa"
                res = self.dp(s, i, p, j + 2, memo)
            # case 2: 无 * 通配符，匹配无法进行下去了
            else:
                res = False

        # 将当前结果记入备忘录
        memo[i][j] = res

        # 返回当前节点结果
        return res

    def isMatch(self, s: str, p: str) -> bool:
        """
        Time O(m * n)
        Space O(m * n)
        同思路1，只是换成自底向上的带返回值的后续遍历DP写法。通过返回值来判断是否存在合理的path。详细见注释。
        """
        m, n = len(s), len(p)
        # 构建备忘录
        memo = [[-1] * n for _ in range(m)]
        # 指针 i，j 从索引 0 开始移动
        return self.dp(s, 0, p, 0, memo)


s = Solution2()
print(s.isMatch(s="aa", p="a"))
print(s.isMatch(s="aa", p="a*"))
print(s.isMatch(s="aaa", p="ab*a*c*a"))
