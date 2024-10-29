from typing import List


class Solution:
    def remove_adj_star(self, p: str) -> str:
        if not p:
            return ""

        filtered_p = p[0]
        for i in range(1, len(p)):
            if p[i] == '*' and p[i - 1] == '*':
                continue
            filtered_p += p[i]

        return filtered_p

    def dp(self, s: str, i: int, p: str, j: int, memo: List[List[int]]) -> bool:
        # 同时都走到底了，返回true
        if j == len(p) and i == len(s):
            return True
        # 字符走到底了
        if i == len(s):
            # check pattern是不是剩下的都是 '*'，这里和10不一样，因为不会出现 'a*'的情况，在这直接 'a*' -> '*'
            for k in range(j, len(p)):
                if p[k] != '*':
                    return False
            # 如果都不是上述情况，直接返回true
            return True
        # 如果pattern走到底了，string没有到达，返回false
        if j == len(p):
            return False

        # 查备忘录，防止重复计算
        if memo[i][j] != -1:
            return bool(memo[i][j])

        res = False
        if s[i] == p[j] or p[j] == '?':
            # s[i] 和 p[j] 完成匹配，直接判断下一个字符
            res = self.dp(s, i + 1, p, j + 1, memo)
        elif p[j] == '*':
            # s[i] 和 p[j] 不匹配，但 p[j] 是通配符 *
            # 可以匹配 0 个或多个 s 中的字符，
            # 只要有一种情况能够完成匹配即可，第一个对应是匹配多个，第二个对应匹配0个
            res = self.dp(s, i + 1, p, j, memo) or self.dp(s, i, p, j + 1, memo)

        # 将 s[i] 和 p[j] 的匹配结果存储备忘录
        memo[i][j] = res

        return res

    def isMatch(self, s: str, p: str) -> bool:
        """
        Time O(m * n)
        Space O(m * n)
        同思路第10题思路，这里的 ? 通配符就是第 10 题的 .，这里的 * 就是第 10 题的 .? 组合，所以直接套用第10题的解法。
        唯一区别就是这里可能出现很多 * 连续出现的情况，很容易看出连续多个 * 和一个 * 的通配效果是一样的，
        所以我们可以提前删除连续的 * 以便提升一些效率
        """
        if not p:
            return not s
        # 将 p 中相邻的 * 去除，以提升效率
        filtered_p = self.remove_adj_star(p)
        m, n = len(s), len(filtered_p)
        # 备忘录初始化为 -1
        memo = [[-1] * n for _ in range(m)]
        # 执行自顶向下带备忘录的动态规划
        return self.dp(s, 0, filtered_p, 0, memo)


s = Solution()
print(s.isMatch(s="aa", p="a"))
print(s.isMatch(s="aa", p="*"))
print(s.isMatch(s="cb", p="?a"))
