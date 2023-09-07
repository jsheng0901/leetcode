class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Time O(n^2)
        Space O(n^2)
        dp[i][j]：表示区间范围[i,j]（注意是左闭右闭）的子串是否是回文子串，如果是dp[i][j]为true，否则为false。
        dp[i][j]初始化为false，这样就不用更新s[i] != s[j]的情况
        当s[i]与s[j]相等时，这就复杂一些了，有如下三种情况:
            情况一：下标i 与 j相同，同一个字符例如a，当然是回文子串
            情况二：下标i 与 j相差为1，例如aa，也是文子串
            情况三：下标：i 与 j相差大于1的时候，例如cabac，此时s[i]与s[j]已经相同了，
            我们看i到j区间是不是回文子串就看aba是不是回文就可以了，那么aba的区间就是 i+1 与 j-1区间，
            这个区间是不是回文就看dp[i + 1][j - 1]是否为true。
        """
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        # dp[i + 1][j - 1] 在 dp[i][j]的左下角，所以遍历顺序一定是从下到上，从左到右遍历，这样保证dp[i + 1][j - 1]都是经过计算的。
        # 并且只会填充dp矩阵右上半部分。因为根据dp数组定义，j一定大于等于i。
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:          # 情况一 和 情况二
                        dp[i][j] = True
                        result += 1
                    elif dp[i + 1][j - 1]:  # 情况三
                        dp[i][j] = True
                        result += 1

        return result


s = Solution()
print(s.countSubstrings(s="aaa"))
