class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """双指针，滑动窗口，每次维护一个没有重复字符的窗口，并且统计这个窗口里面每个字符的出现次数，必须都是1
        如果当前遍历到的字符从未出现过，那么直接扩大右边界；
        如果当前遍历到的字符出现过，则缩小窗口（左边索引向右移动），然后继续观察当前遍历到的字符；
        重复（1）（2），直到窗口内无重复元素；
        维护一个全局最大窗口 res，每次用出现过的窗口大小来更新结果 res，最后返回 res 获取结果;
        最后返回 res 即可
        """
        hash_map = {}
        result = 0
        left = 0
        for right in range(len(s)):
            while s[right] in hash_map and hash_map[s[right]] > 0:
                hash_map[s[left]] -= 1
                left += 1

            if s[right] not in hash_map:
                hash_map[s[right]] = 1
            else:
                hash_map[s[right]] += 1

            result = max(result, right - left + 1)

        return result