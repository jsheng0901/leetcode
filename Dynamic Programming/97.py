class Solution:
    def dp(self, s1, i, s2, j, s3, memo):
        k = i + j
        # base case，s3 构造完成
        if k == len(s3):
            return True

        # 查备忘录，如果已经计算过，直接返回
        if memo[i][j] != -1:
            return memo[i][j]

        # 初始化本层结果为 false
        res = False
        # 如果，s1[i] 可以匹配 s3[k]，那么填入 s1[i] 试一下
        if i < len(s1) and s1[i] == s3[k]:
            res = self.dp(s1, i + 1, s2, j, s3, memo)

        # 如果，s1[i] 匹配不了，s2[j] 可以匹配，那么填入 s2[j] 试一下
        if j < len(s2) and s2[j] == s3[k]:
            res = res or self.dp(s1, i, s2, j + 1, s3, memo)

        # 如果 s1[i] 和 s2[j] 都匹配不了，则返回 false
        # 将结果存入备忘录
        memo[i][j] = res

        return res

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Time O(n * m)
        Space O(n * m)
        双指针插入是否能构成一个新的string。这里有个难点在于，跟普通的数组/链表双指针技巧不同的是，这里需要穷举所有情况。
        比如 s1[i], s2[j] 都能匹配 s3[k] 的时候，应该选谁来匹配，才能完全合并出 s3。需要一个递归函数来穷举双指针的匹配过程，
        然后用一个备忘录消除递归过程中的重叠子问题。
        """
        m, n = len(s1), len(s2)
        # 如果长度对不上，必然不可能
        if m + n != len(s3):
            return False

        # 备忘录，其中 -1 代表未计算，这里需要额外的一行和一列因为递归的时候进入下一个指针的时候会越界，但是我们并不知道是否还要继续，
        # 不能直接返回，因为 s1 越界可能代表 s1 走完了，但是 s2 还可以继续走。
        memo = [[-1] * (n + 1) for _ in range(m + 1)]

        return self.dp(s1, 0, s2, 0, s3, memo)


s = Solution()
print(s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
print(s.isInterleave(s1="", s2="", s3=""))
print(s.isInterleave(s1="", s2="", s3="a"))
print(s.isInterleave(s1="a", s2="", s3="c"))
print(s.isInterleave(s1="a", s2="", s3="a"))
print(s.isInterleave(s1="", s2="b", s3="b"))
