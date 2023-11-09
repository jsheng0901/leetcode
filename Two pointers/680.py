class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Time O(2n) -> O(n)
        Space O(1)
        双指针指针判断，第一次loop遇到不同的时候只动右指针，第二次loop遇到不同的时候只动左指针，然后取最小值，判断是否小于等于1
        此题可以用dp方法找出最长回文子序列(subsequence)再用原始长度减去这个结果，判断是否大于一，不过会超时
        """
        left = 0
        right = len(s) - 1
        count1 = 0
        # 第一次loop
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                count1 += 1
                right -= 1
        if count1 <= 1:  # 如果已经小于，则已经找到可行方案，直接返回
            return True

        left = 0
        right = len(s) - 1
        count2 = 0
        # 第二次loop
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                count2 += 1
                left += 1
                if count2 > 1:  # 如果已经大于则不可能，直接返回
                    return False

        # 只需要return第二次count是否等于1，因为如果第一次count等于1，则根本不会到第二次count
        return count2 == 1


class Solution2:
    def check_palindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        """
        Time O(n)
        Space O(1)
        同样的思路，只是当遇到不相等的字符的时候，直接判断左指针往前走一步，或者右指针往左跳一步，判断是否是回文，有一个是回文即可。
        这里其实思路就等同于回溯的切割，找到一次切割的所有组合，如果新地组合是回文则回溯返回bool来判断是否有合理的一条path。
        """

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                left = self.check_palindrome(s, i + 1, j)
                right = self.check_palindrome(s, i, j - 1)
                return left or right
            i += 1
            j -= 1

        return True


s = Solution2()
print(s.validPalindrome(s="abca"))
