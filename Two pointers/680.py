class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        左右指针判断，第一次不同的时候只动右指针，第二次不同的时候只动左指针，然后取最小值，判断是否小于等于1
        此题可以用dp方法找出最长回文子序列(subsequence)再用原始长度减去这个结果，判断是否大于一，不过会超时
        dp: O(n^2)
        two points: O(2n) --> O(n)
        """
        left = 0
        right = len(s) - 1
        count1 = 0
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                count1 += 1
                right -= 1
        if count1 <= 1:     # 如果已经小于，则已经找到可行方案，直接返回
            return True

        left = 0
        right = len(s) - 1
        count2 = 0
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                count2 += 1
                left += 1
                if count2 > 1:      # 如果已经大于则不可能，直接返回
                    return False

        return min(count1, count2) <= 1
