class Solution:
    def palindrome(self, s, left, right):
        # 和判断回文不一样的是，这里从中间往两边走
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1: right]

    def longestPalindrome(self, s: str) -> str:
        """
        Time O(n^2)
        Space O(n)
        双指针版本，每一次从中间往两边判断最长回文，同时判断奇数情况回文和偶数情况回文，然后判断长度更新最长回文的结果。
        """
        result = ''
        for i in range(len(s)):
            even_s = self.palindrome(s, i, i)  # 偶数情况回文
            odd_s = self.palindrome(s, i, i + 1)  # 奇数情况回文
            result = result if len(result) > len(even_s) else even_s  # 更新结果
            result = result if len(result) > len(odd_s) else odd_s  # 更新结果

        return result


s = Solution()
print(s.longestPalindrome(s="babad"))
