class Solution1:
    def is_valid(self, sub):

        # 其它判断同91题
        if len(sub) > 2:
            return False
        if sub[0] == '0':
            return False
        if "*" not in sub and int(sub) > 26:
            return False
        # case "7*" 这种情况，不合理
        if len(sub) == 2 and sub[1] == "*" and sub[0] != "*" and int(sub[0]) > 2:
            return False

        return True

    def dp(self, s, start_index, memo, mod):
        # 走到底了，找到一条合理的path，返回1
        if start_index >= len(s):
            return 1

        # 之前切割过记录进备忘录，返回结果
        if memo[start_index] != -1:
            return memo[start_index]

        # 累计计算有多少条合理的返回的子path
        sub_res = 0
        for i in range(start_index, len(s)):
            sub = s[start_index: i + 1]
            # 合理地切割，继续递归
            if self.is_valid(sub):
                # 有 "*" 在substring里面
                if "*" in sub:
                    # 如果只有一个 "*" 号的情况，可以替代9种数字
                    if len(sub) == 1:
                        sub_res += self.dp(s, i + 1, memo, mod) * 9 % mod
                    else:
                        # 如果只有两个 "**" 号的情况，可以替代15种数字，11 - 26
                        if sub == "**":
                            sub_res += self.dp(s, i + 1, memo, mod) * 15 % mod
                        # 如果只有一个 "*" 号长度为2并且第一个是 "*" 的情况
                        elif sub[0] == "*":
                            # 比如 "*7"，第一个 "*" 只能是1，就一种情况
                            if int(sub[1]) > 6:
                                sub_res += self.dp(s, i + 1, memo, mod) * 1 % mod
                            # 比如 "*5"，第一个 "*" 可以是1或者2，两种情况
                            else:
                                sub_res += self.dp(s, i + 1, memo, mod) * 2 % mod
                        # 如果只有一个 "*" 号长度为2并且第二个是 "*" 的情况
                        elif sub[1] == "*":
                            # 比如 "1*"，第二个 "*" 可以是1 - 9，总共9种情况
                            if sub[0] == "1":
                                sub_res += self.dp(s, i + 1, memo, mod) * 9 % mod
                            # 比如 "2*"，第二个 "*" 可以是1 - 6，总共6种情况
                            elif sub[0] == "2":
                                sub_res += self.dp(s, i + 1, memo, mod) * 6 % mod
                else:
                    # 没有 "*" 在substring里面，同91题
                    sub_res += self.dp(s, i + 1, memo, mod) % mod

        memo[start_index] = sub_res % mod

        return memo[start_index]

    def numDecodings(self, s: str) -> int:
        """
        Time O(n)
        Space O(n)
        同91题，只是每次取sub string的时候需要判断多种情况，详细见注释，但是这个解法在 leetcode 上会TLE。
        """
        memo = [-1] * len(s)
        mod = 10 ** 9 + 7
        res = self.dp(s, 0, memo, mod) % mod

        return res


class Solution2:
    def numDecodings(self, s: str) -> int:
        """
        Time O(n)
        Space O(n)
        同思路1，只是换成线性写法，自顶向下写。
        """
        if len(s) == 0 or (len(s) > 1 and s[0] == '0'):
            return 0

        mod = 10 ** 9 + 7
        # 初始化一个长度等于s+1的dp数组
        dp = [0] * (len(s) + 1)
        # 初始化第0为1
        dp[0] = 1
        dp[1] = 9 if s[0] == "*" else 0 if s[0] == "0" else 1

        for i in range(1, len(s)):
            if s[i] == "*":
                dp[i + 1] = dp[i] * 9 % mod
                if s[i - 1] == "1":
                    dp[i + 1] += 9 * dp[i - 1] % mod
                elif s[i - 1] == "2":
                    dp[i + 1] += 6 * dp[i - 1] % mod
                elif s[i - 1] == "*":
                    dp[i + 1] += 15 * dp[i - 1] % mod
            else:
                dp[i + 1] = 0 if s[i] == "0" else dp[i]
                if s[i - 1] == "1":
                    dp[i + 1] += dp[i - 1] % mod
                elif s[i - 1] == "2" and int(s[i]) <= 6:
                    dp[i + 1] += dp[i - 1] % mod
                elif s[i - 1] == "*":
                    dp[i + 1] += (2 if int(s[i]) <= 6 else 1) * dp[i - 1] % mod

        return dp[-1] % mod


s = Solution2()
print(s.numDecodings(s="1*72*"))
print(s.numDecodings(s="*"))
print(s.numDecodings(s="**"))
print(s.numDecodings(s="1*"))
print(s.numDecodings(s="2*"))
