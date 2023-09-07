class Solution:
    def palindrome(self, s, left, right):
        result = 0
        # 和判断回文不一样的是，这里从中间往两边走
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            result += 1     # 每次进loop就意味着找到一个回文，结果+1

        return result

    def countSubstrings(self, s: str) -> int:
        """
        Time O(n^2)
        Space O(1)
        双指针版本，每一次从中间往两边判断回文，同时判断奇数情况回文和偶数情况回文，然后计算有多少个回文结果。
        """
        result = 0
        for i in range(len(s)):
            even_count = self.palindrome(s, i, i)  # 偶数情况回文
            odd_count = self.palindrome(s, i, i + 1)  # 奇数情况回文
            result += even_count + odd_count

        return result


s = Solution()
print(s.countSubstrings(s="babad"))
