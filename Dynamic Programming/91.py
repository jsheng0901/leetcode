class Solution:
    def __init__(self):
        self.count = 0

    def numDecodings1(self, s: str) -> int:
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

    def isValid(self, sub):

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
            if self.isValid(sub):
                self.backtracking(s, i + 1)

    def numDecodings2(self, s: str) -> int:
        """
        Time O(n!)
        Space O(n)
        回溯做法，列出所有组合，并check是否valid，如果valid并且走到最后一个index，则说明找到其中一条从头到底的路径，此时计数。
        """

        self.backtracking(s, 0)

        return self.count


s = Solution()
print(s.numDecodings2(s="226"))
