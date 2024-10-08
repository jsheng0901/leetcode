class Solution1:
    def longestPalindrome(self, s: str) -> str:
        """
        Time O(n^2)
        Space O(n^2)
        此题同647，一模一样，一个找多少个回文，一个找最长回文。
        dp[i][j]：表示区间范围[i,j]的子串是否是回文子串，如果是dp[i][j]为true，否则为false
        当s[i]与s[j]不相等，dp[i][j]一定是false。
        当s[i]与s[j]相等时，这就复杂一些了，有如下三种情况
        情况一：下标i 与 j相同，同一个字符例如a，当然是回文子串
        情况二：下标i 与 j相差为1，例如aa，也是文子串
        情况三：下标：i 与 j相差大于1的时候，例如cabac，此时s[i]与s[j]已经相同了，
                    我们看i到j区间是不是回文子串就看aba是不是回文就可以了，那么aba的区间就是 i+1 与 j-1区间，
                    这个区间是不是回文就看dp[i + 1][j - 1]是否为true。

        此题最重要的还有loop的顺序，一定是从下到上，再从左到右遍历
        """
        dp = [[False] * len(s) for _ in range(len(s))]
        max_length = 0
        left = 0
        right = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                    elif dp[i + 1][j - 1]:
                        dp[i][j] = True

                if dp[i][j] and j - i + 1 > max_length:
                    max_length = j - i + 1
                    left = i
                    right = j

        return s[left: right + 1]


class Solution2:
    def palindrome(self, s, left, right):
        # 和判断回文不一样的是，这里从中间往两边走
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1: right]

    def longestPalindrome(self, s: str) -> str:
        """
        Time O(n^2)
        Space O(1)
        双指针版本，每一次从中间往两边判断最长回文，同时判断奇数情况回文和偶数情况回文，然后判断长度更新最长回文的结果。
        """
        result = ''
        for i in range(len(s)):
            even_s = self.palindrome(s, i, i)  # 偶数情况回文
            odd_s = self.palindrome(s, i, i + 1)  # 奇数情况回文
            result = result if len(result) > len(even_s) else even_s  # 更新结果
            result = result if len(result) > len(odd_s) else odd_s  # 更新结果

        return result


s = Solution2()
print(s.longestPalindrome(s="babad"))
