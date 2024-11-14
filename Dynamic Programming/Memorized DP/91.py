class Solution1:
    def __init__(self):
        self.count = 0

    def is_valid(self, sub):

        if len(sub) > 2:
            return False
        if sub[0] == '0':
            return False
        if int(sub) > 26:
            return False

        return True

    def backtracking(self, s, start_index):
        if start_index >= len(s):
            self.count += 1

        for i in range(start_index, len(s)):
            sub = s[start_index: i + 1]
            if self.is_valid(sub):
                self.backtracking(s, i + 1)

    def numDecodings(self, s: str) -> int:
        """
        Time O(n!) 此题回溯就是排列问题，每一行树从n, n-1, n-2, ...一次递减，最终是n!
        Space O(n) 递归深度为n，所以系统栈所用空间为O(n)
        回溯做法，列出所有组合，并check是否valid，如果valid并且走到最后一个index，则说明找到其中一条从头到底的路径，此时计数。
        """

        self.backtracking(s, 0)

        return self.count


class Solution2:
    def numDecodings(self, s: str) -> int:
        """
        Time O(n)
        Space O(n)
        回溯的做法超时，dp的做法是，当前数字有前一个和前两数字的情况来决定，和爬楼梯一个道理
        dp[i]的含义是走到i的时候有多少种组合方法
        """

        if len(s) == 0 or (len(s) > 1 and s[0] == '0'):
            return 0

        # 初始化一个长度等于s+1的dp数组
        dp = [0] * (len(s) + 1)
        # 初始化第0为1
        dp[0] = 1
        # 初始化第1才是s的第一个字母
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(dp)):
            # 如果前一个为0则当前字母没办法和前一个字母组合成一个valid的数字，所以为0
            # 如果不为0，则说明前一个到当前这个只有一种方法，延续前一个状态
            dp[i] = 0 if s[i - 1] == '0' else dp[i - 1]
            # 如果前两个组成的字母可以在10-26范围内，说明可以条两步，更新当前dp[i]
            two_digit = int(s[i - 2: i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]


class Solution3:
    def is_valid(self, sub):

        if len(sub) > 2:
            return False
        if sub[0] == '0':
            return False
        if int(sub) > 26:
            return False

        return True

    def dp(self, s, start_index, memo):
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
                sub_res += self.dp(s, i + 1, memo)

        memo[start_index] = sub_res

        return memo[start_index]

    def numDecodings(self, s: str) -> int:
        """
        Time O(n)
        Space O(n)
        同思路2，换成自底向上的写法。带备忘录的回溯就是DP的思路。
        """
        memo = [-1] * len(s)
        res = self.dp(s, 0, memo)

        return res


s = Solution3()
print(s.numDecodings(s="226"))
