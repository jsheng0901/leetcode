
class Solution:
    def get_possible_length(self, s):
        # 找到所有长度组合情况
        # 这里接近了分治的思路，一直把一个string拆解到最小单位只有一个数字的时候再返回，再叠加
        possible_length = [int(s)]
        for i in range(1, len(s)):
            tmp_list = [x + y for x in self.get_possible_length(s[:i]) for y in self.get_possible_length(s[i:])]
            possible_length += tmp_list

        return list(set(possible_length))

    def dp(self, s1, s2, p1, p2, diff, memo):
        # 走到底并且没有差距，返回true否则返回false
        if p1 == len(s1) and p2 == len(s2):
            return diff == 0

        # 记录进备忘录
        if (p1, p2, diff) in memo:
            return memo[(p1, p2, diff)]

        # 初始化当前节点的返回值
        res = False
        # 如果指针1是数字
        if p1 < len(s1) and s1[p1].isdigit():
            tmp = p1
            # 找到这个数字的string，比如 '123'
            while tmp < len(s1) and s1[tmp].isdigit():
                tmp += 1
            # 找出所有数字可能的长度组合
            possible_length = self.get_possible_length(s1[p1: tmp])
            # 遍历所有组合情况
            for l in possible_length:
                res = res or self.dp(s1, s2, tmp, p2, diff - l, memo)
        # 如果指针2是数字
        elif p2 < len(s2) and s2[p2].isdigit():
            tmp = p2
            while tmp < len(s2) and s2[tmp].isdigit():
                tmp += 1
            possible_length = self.get_possible_length(s2[p2: tmp])
            for l in possible_length:
                res = res or self.dp(s1, s2, p1, tmp, diff + l, memo)
        # 如果指针都不是数字，并且相等的情况
        elif diff == 0 and p1 < len(s1) and p2 < len(s2) and s1[p1] == s2[p2]:
            res = res or self.dp(s1, s2, p1 + 1, p2 + 1, 0, memo)
        # 如果指针都不是数字，并且第二个指针走到更快的情况下
        elif diff > 0 and p1 < len(s1):
            res = res or self.dp(s1, s2, p1 + 1, p2, diff - 1, memo)
        # 如果指针都不是数字，并且第一个指针走到更快的情况下
        elif diff < 0 and p2 < len(s2):
            res = res or self.dp(s1, s2, p1, p2 + 1, diff + 1, memo)

        memo[(p1, p2, diff)] = res

        return res

    def possiblyEquals(self, s1: str, s2: str) -> bool:
        """
        Time O(n^2 * diff)
        Space O(n^2 * diff)
        时间复杂度由memo的大小构成。此题很巧妙，这里的diff记录的是指针1和指针2的距离差，假设指针1往前走，difference变成负数，
        相反指针2往前走，就应该缩短距离差也就是 + 正数。最终应该是两个都走到最后，并且没有任何difference。记录所有切割的情况并且对比返回值。
        这里还有个巧妙的地方是如何生成所有可能的长度组合对于一个"123"类型的数字。
        这里应该可能有 [123, 1 + 2 + 3, 1 + 23, 12 + 3, 1 + 2 + 3] -> [6, 15, 24, 123] 四种情况的长度组合，需要遍历每一种组合。
        举个例子：
        +----+----+-------+-------+----------------------------------+
        | i  | j  | s1[i] | s2[j] | diff (at the start of iteration) |
        +----+----+-------+-------+----------------------------------+
        | 0  | 0  | 'a'   | 'a'   |                                0 |
        | 1  | 1* |  3    | 'b'   |                                0 |
        | 2* | 1  | 'e'   | 'b'   |                               -3 |
        | 2* | 2  | 'e'   |  2    |                               -2 |
        | 2* | 3  | 'e'   |  1    |                                0 |
        | 2  | 4* | 'e'   |  ---  |                                1 |
        | 3  | 4  | ---   |  ---  |                                0 |
        +----+----+-------+-------+----------------------------------+
        """
        memo = {}
        return self.dp(s1, s2, 0, 0, 0, memo)


s = Solution()
print(s.possiblyEquals(s1="l123e", s2="44"))
print(s.possiblyEquals(s1="a5b", s2="c5b"))
