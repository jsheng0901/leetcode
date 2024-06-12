from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        Time O(n)
        Space O(1)
        滑动窗口模版题，一直移动右指针统计窗口内字符出现的频率，如果窗口内超过两个key，则说明要开始缩小窗口也就是左指针。注意这里要记录字符的
        频率，当频率为0的时候要删除这个key。窗口内最多3个pair，所以空间复杂度是O(1)。
        """
        # 初始化窗口
        window = defaultdict(int)
        # 左右指针
        left = 0
        right = 0
        # 记录最长长度
        longest_substring = float('-inf')
        while right < len(s):
            # 进窗口的字符
            c = s[right]
            # 右指针移动
            right += 1
            # 更新窗口
            window[c] += 1
            # 满足条件，更新长度
            if len(window) <= 2:
                longest_substring = max(longest_substring, right - left)

            # 不满足条件，开始缩短窗口，左指针移动
            while len(window) > 2:
                # 出去的字符
                d = s[left]
                # 左指针移动
                left += 1
                # 更新窗口
                window[d] -= 1
                # 如果为0，说明当前字符在窗口内已经完全移除
                if window[d] <= 0:
                    # 删除当前字符key
                    del window[d]

        return longest_substring


s = Solution()
print(s.lengthOfLongestSubstringTwoDistinct(s="eceba"))
print(s.lengthOfLongestSubstringTwoDistinct(s="ccaabbb"))
