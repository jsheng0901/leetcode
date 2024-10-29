from collections import Counter


class Solution1:
    def dp(self, string):
        # 切到底了，直接返回单个字符
        if len(string) <= 1:
            return [string]

        # 存储当前节点所有切割过的结果
        sub = set()
        for i in range(len(string) - 1):
            # 左边切割过的结果
            left_res = self.dp(string[:i + 1])
            # 右边切割过的结果
            right_res = self.dp(string[i + 1:])
            # 找到所有组合
            for left in left_res:
                for right in right_res:
                    # 不swap的结果
                    sub.add(left + right)
                    # swap的结果
                    sub.add(right + left)

        return sub

    def isScramble(self, s1: str, s2: str) -> bool:
        """
        Time O(n^3)
        Space O(n)
        后续遍历方法返回切割后的结果，进行叠加，计算出所有s1切割后的结果，最后判断里面是否有s2出现过。时间上其实应该更快，但是空间上
        会溢出，因为要存储每次节点切割之后的所有结果。
        """
        all_res = self.dp(s1)

        if s2 in all_res:
            return True
        else:
            return False


class Solution2:
    def dp(self, string1, string2, i, j, length, memo):
        # 判断两个子串是否相等
        if string1[i: i + length] == string2[j: j + length]:
            return True

        # 判断是否存在字符 c 在两个子串中出现的次数不同
        if Counter(string1[i: i + length]) != Counter(string2[j: j + length]):
            return False

        # 出现过重复的切割
        if memo[length][i][j] != -1:
            return memo[length][i][j]

        sub = False
        # 枚举分割位置
        for index in range(1, length):
            # 不交换的情况
            no_swap_left = self.dp(string1, string2, i, j, index, memo)
            no_swap_right = self.dp(string1, string2, i + index, j + index, length - index, memo)
            # 如果找到一条成功的path，直接结束当前切割，因为我们只需要找到一条合理的path
            if no_swap_left and no_swap_right:
                sub = True
                break

            # 交换的情况
            swap_left = self.dp(string1, string2, i, j + length - index, index, memo)
            swap_right = self.dp(string1, string2, i + index, j, length - index, memo)
            # 同上
            if swap_left and swap_right:
                sub = True
                break

        # 记录进备忘录
        memo[length][i][j] = sub

        return sub

    def isScramble(self, s1: str, s2: str) -> bool:
        """
        Time O(n^4)
        Space O(n^3)
        方法1需要大量的空间来存储所有切割过的结果，实际上我们可以两个string一起切割，来进行判断是否相等，这样就只需要返回path是否valid即可。
        三种情况判断是否和谐，
        如果 s1 = s2，那么它们是「和谐」的；
        如果 s1 和 s2 的长度不同，那么它们一定不是「和谐」的；
        如果 s1 中某个字符 c 出现了 x1 次，而 c 在 s2 中出现了 x2 次，且 x1 != x2，那么它们一定不是「和谐」的。
        这是因为任意操作都不会改变一个字符串中的字符种类以及数量。
        然后我们从两个角度对比分割s1后的结果，第一种是不swap，第二种是swap。每一种分别对应到s2分割后的结果上。
        dp[l][i][j]表示对于长度为l的字符串，s1为i的起点和s2为j的起点切割后对应是否和谐。详细见注释。
        """
        # 备忘录有三种状态
        memo = [[[-1] * len(s1) for _ in range(len(s1))] for _ in range(len(s1) + 1)]

        res = self.dp(s1, s2, 0, 0, len(s1), memo)

        return res


s = Solution2()
print(s.isScramble(s1="great", s2="rgeat"))
print(s.isScramble(s1="abcde", s2="caebd"))
print(s.isScramble(s1="a", s2="a"))
