from collections import defaultdict


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time O(n)
        Space O(len(s))
        双指针，滑动窗口，每次维护一个没有重复字符的窗口，并且统计这个窗口里面每个字符的出现次数，必须都是1
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


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time O(n)
        Space O(len(s))
        同样是双指针，规范化双指针模板。区别与其它模板题目，不需要valid和need来判断是否满足条件，再更新result，
        而是在收缩窗口完成后更新 result，因为窗口收缩的 while 条件是存在重复元素，换句话说收缩完成后一定保证窗口中没有重复。
        """
        # 构建字典记录窗口中各字符出现的次数
        window = defaultdict(int)
        # 窗口的左右边界
        left, right = 0, 0
        # 用于记录结果
        result = 0

        while right < len(s):
            c = s[right]
            right += 1
            # 更新窗口和字符的出现次数
            window[c] += 1

            # 判断窗口是否需要收缩
            while window[c] > 1:
                d = s[left]
                left += 1
                # 更新窗口和字符的出现次数
                window[d] -= 1

            # 更新结果，每次在最后更新，因为如果窗口内不符合要求，则会在前面先弹出所有不符合的字符
            result = max(result, right - left)

        return result
