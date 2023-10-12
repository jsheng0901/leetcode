from collections import defaultdict
from typing import List


class Solution:
    def left_bound(self, arr, target):
        # 查找左侧边界的二分查找，这里和传统左边界不一样的地方是，可能会出现target不存在的情况。
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] == target:
                right = mid - 1
            elif arr[mid] > target:
                right = mid - 1
        # 这里我们只需要判断有没有越界即可，不需要额外判断 arr[left] != target 的情况，因为本来target就可能不存在。
        if left >= len(arr):
            return -1
        # 此时返回值 left刚好是比 target 大的最小元素索引。
        else:
            return left

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """
        Time O(m * log(n))
        Space O(n)
        传统双指针 O(n) 搜索 + loop 整个list的写法会超时。主要是有个word很长。
        先用一个hash map记录s中所有元素出现的位置，从小到大记录index。
        二分法查找左边界，刚好可以找当 目标 val 不存在时，得到的索引恰好是比 val 大的最小元素索引。
        就是说如果在数组 [0,1,3,4] 中搜索元素 2，算法会返回索引 2，也就是元素 3 的位置，元素 3 是数组中大于 2 的最小元素。
        所以我们可以利用二分搜索避免线性扫描。
        """
        # 对 s 进行预处理，记录字符 c 的所有出现位置
        index = defaultdict(list)
        for i in range(len(s)):
            c = s[i]
            index[c].append(i)

        # 统计符合要求的 words
        # 记录符合要求的单词数量
        res = 0
        for word in words:
            # 指向 s 中当前查找的字符的位置
            j = 0
            # 记录已匹配的单词长度
            valid_c = 0
            for i in range(len(word)):
                # 当前字符
                c = word[i]
                # 如果 s 中不存在单词当前字符，则不可能匹配
                if c not in index:
                    break
                # 二分查找 字符c 第一次出现的位置
                pos = self.left_bound(index[c], j)
                # 如果没找到，则已经匹配失败了
                if pos == -1:
                    break
                # 如果找到匹配长度 +1
                valid_c += 1
                # 同时更新下一个 s 中查找字符的位置，pos 是找到的下标，所以要加1，指向下一个位置
                j = index[c][pos] + 1
            # 如果整个单词匹配结束，说明这是一个符合要求的单词
            if valid_c == len(word):
                res += 1

        # 返回符合要求的单词数量
        return res


s = Solution()
print(s.numMatchingSubseq(s="abcde", words=["a", "bb", "acd", "ace"]))
print(s.numMatchingSubseq(s="dsahjpjauf", words=["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]))
