from collections import defaultdict


class Solution1:
    def get_max_num_unique_letters(self, s):
        seen = set()
        for ch in s:
            seen.add(ch)

        return len(seen)

    def longestSubstring(self, s: str, k: int) -> int:
        """
        Time O(26 * n) --> O(n)
        Space O(26) --> O(1)
        此题非常巧妙，如何定义滑动窗口的扩大或者收缩是最重要的部分。我们先找到总共有多少个不同的字符，然后遍历每一种情况下的窗口，
        所以当窗口内不同字符的个数大于我们要求的个数的时候，就开始收缩窗口。详细见注释。
        """
        # 计算最多多少个不同的字符
        max_num_unique_letters = self.get_max_num_unique_letters(s)
        res = 0
        # 遍历当前不同字符的个数，比如如果当前字符串满足1个不同的字符，那么最长的substring是多少，以此类推。
        for cur_unique in range(1, max_num_unique_letters + 1):
            # 初始化双指针
            left = 0
            right = 0
            # 当前窗口内不同字符的个数
            unique = 0
            # 当前窗口内满足条件的不同字符个数
            need = 0
            # 初始化窗口
            window = defaultdict(int)
            while right < len(s):
                # 进窗口的指针
                c = s[right]
                # 右指针 +1
                right += 1
                # 如果是全新的字符，不同字符个数 +1
                if c not in window:
                    unique += 1
                # 更新窗口内字符出现的频率
                window[c] += 1
                # 如果符合出现频率要求等于k
                if window[c] == k:
                    # 满足条件的不同字符个数 +1
                    need += 1
                # 如果当前字符个数满足我们设置的当前遍历不同字符个数并且窗口内所有字符都满足条件
                if unique == cur_unique and unique == need:
                    # 找到一个合理的substring，更新长度
                    res = max(res, right - left)

                # 如果不同字符个数大于我们当前的设置，开始收缩窗口
                while unique > cur_unique:
                    # 弹出的字符
                    d = s[left]
                    # 左指针 +1
                    left += 1
                    # 如果弹出的这个刚好满足条件，弹出后一定不再满足条件
                    if window[d] == k:
                        # 满足条件的不同字符个数 -1
                        need -= 1
                    # 更新窗口内字符出现的频率
                    window[d] -= 1
                    # 如果更新完后，当前字符频率为0
                    if window[d] == 0:
                        # 说明不同字符个数 -1
                        unique -= 1
                        # 这里Python因为用了字典来记录窗口内频率，当频率为0的时候需要删除此key，
                        # 不然后续计算unique个数的时候会少算，因为会有 key: 0 的这对 pair留下来。
                        del window[d]

        return res


class Solution2:
    def longest_substring_split(self, s, left, right, k):
        # 构建窗口，记录频率
        window = defaultdict(int)
        # 统计每个字符出现的频率
        for i in range(left, right):
            window[s[i]] += 1

        # 找到第一个不符条件的字符
        for j in range(left, right):
            # 如果符合条件，跳过
            if window[s[j]] >= k:
                continue
            # 第一个不符合条件的字符index的下一个index
            mid = j + 1
            # 如果下一个index都不符合条件，loop直到符合的index
            while mid < right and window[s[mid]] < k:
                mid += 1

            # 左子树的结果
            left = self.longest_substring_split(s, left, j, k)
            # 右子树的结果
            right = self.longest_substring_split(s, mid, right, k)
            # 返回最大值
            return max(left, right)

        # 如果不存在不符合条件的字符，说明找到了合理的substring，直接返回长度
        return right - left

    def longestSubstring(self, s: str, k: int) -> int:
        """
        Time O(n^2)
        Space O(n)
        分治的思想，对于每一个不合理的字符，我们直接处理这个字符两边的substring，一直split，直到有一个substring满足所有条件，此时类似后续
        遍历，分治就是后续遍历的返回思路，把所有结果层次网上返回，取每个子节点返回值的最大值即可。分治的核心思想，不需要考虑每次情况，
        直接考虑最小划分下的返回结果，然后层层网上返回。
        """
        return self.longest_substring_split(s, 0, len(s), k)


s = Solution1()
print(s.longestSubstring(s="aaabb", k=3))
print(s.longestSubstring(s="baaabcb", k=3))
