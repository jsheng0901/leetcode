class Solution1:
    def isSubsequence1(self, s: str, t: str) -> bool:
        """
        Time O(n)
        Space O(1)
        双指针法。不过本题最好学会dp方法，双指针很简单，一个指针在s, 一个在t，
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
            if p1 == l1:  # 需要提前判断，可能t指针还没走完，s已经到最后了，并且到最后的时候s指针是超过index的，是length
                return True

            if s[p1] == t[p2]:
                p1 += 1

        return p1 == l1

    def isSubsequence2(self, s: str, t: str) -> bool:
        """
        Time O(n)
        Space O(1)
        双指针法另一种写法while loop更好写
        """
        # 双指针起始位置
        p1 = 0
        p2 = 0
        # 双指针都在index内才loop
        while p2 < len(t) and p1 < len(s):
            # 如果相等则s的指针向前走一步
            if t[p2] == s[p1]:
                p1 += 1
            p2 += 1

        return p1 == len(s)


class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Time O(n × m)
        Space O(n × m)
        动态规划法，dp[i][j] 表示以下标i-1为结尾的字符串s，和以下标j-1为结尾的字符串t，相同子序列的长度为dp[i][j]
        当相等的时候用前一位的状态+1，不同的时候用t前一个状态判断，此时相当于t要删除元素，t如果把当前元素t[j - 1]删除，
        那么dp[i][j] 的数值就是 看s[i - 1]与 t[j - 2]的比较结果了，即：dp[i][j] = dp[i][j - 1];
        注意这里不需要s的前一个状态，因为是找s是否是t的子序列。
        """
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1] == len(s)


s = Solution2()
print(s.isSubsequence(s="abc", t="ahbgdc"))
