class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        """双指针法。不过本题最好学会dp方法，双指针很简单，一个指针在s, 一个在t，
        每次loop t，然后判断是否相等，相等则s指针向前走，最后判断s指针有没有走到最后
        """
        l1 = len(s)
        l2 = len(t)
        if l1 == 0:
            return True
        if l2 == 0:
            return False
        p1 = 0
        for p2 in range(l2):
            if p1 == l1:       # 需要提前判断，可能t指针还没走完，s已经到最后了，并且到最后的时候s指针是超过index的，是length
                return True

            if s[p1] == t[p2]:
                p1 += 1

        return p1 == l1


class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        动态规划法，矩阵loop，dp[i][j] 表示以下标i-1为结尾的字符串s，和以下标j-1为结尾的字符串t，相同子序列的长度为dp[i][j]
        当相等的时候用前一位的状态+1，不同的时候用t前一个状态判断，注意这里不需要s的前一个状态，因为是找s是否是t的子序列
        """
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1] == len(s)


