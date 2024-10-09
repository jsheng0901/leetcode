# 滑动窗口模板，直接套用。
# def slidingWindow(s: str):
#     # 用合适的数据结构记录窗口中的数据
#     window = {}
#
#     left = 0
#     right = 0
#
#     while right < len(s):
#         # c 是将移入窗口的字符
#         c = s[right]
#         if c not in window:
#             window[c] = 1
#         else:
#             window[c] += 1
#
#         # 增大窗口
#         right += 1
#
#         # 进行窗口内数据的一系列更新
#         # ...
#
#         # 判断左侧窗口是否要收缩
#         while left < right and window needs shrink:
#             # d 是将移出窗口的字符
#             d = s[left]
#
#             # 缩小窗口
#             left += 1
#
#             # 进行窗口内数据的一系列更新
#             # ...
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Time O(n)
        Space O(n) worst case dictionary存储所有characters
        双指针滑动窗口模版题，先动右指针，直到找到合理的区间包含所有t，然后动左指针一直弹出左边character直到不满足覆盖整个t。
        """
        # 构建两部字典存储需求的字符串个数和窗口里面有的所有字符串情况
        window = defaultdict(int)
        need = defaultdict(int)
        # 更新need字典，把需要的字符串个数加入进去
        for c in t:
            need[c] += 1
        # 构建左闭右开区间[0, 0)此时一开始没有元素在window里面
        left, right = 0, 0
        # 用来记录是否已经满足条件
        valid = 0
        # 记录最小覆盖子串的起始索引及长度
        start = 0
        length = float('inf')

        while right < len(s):
            # c 是将移入窗口的字符
            c = s[right]
            # 扩大窗口
            right += 1

            # 进行窗口内数据的一系列更新
            if c in need:
                # 找到一个元素则窗口字典 +1
                window[c] += 1
                # 如果此字符串满足条件，则valid +1
                if window[c] == need[c]:
                    valid += 1

            # 此时已经说明所有情况都已经满足在window里面，开始判断左侧窗口是否要收缩
            while valid == len(need):
                # 在这里更新最小覆盖子串
                if right - left < length:
                    # 更新最覆盖小子串的起始index
                    start = left
                    length = right - left

                # d 是将移出窗口的字符
                d = s[left]
                # 缩小窗口
                left += 1

                # 进行窗口内数据的一系列更新
                if d in need:
                    # 如果已经字符串已经满足，说明此时弹出的字符d会造成window不满足条件
                    if window[d] == need[d]:
                        # 此时需要valid -1
                        valid -= 1
                    # 同时window字典里面也需要更新
                    window[d] -= 1

        # 返回最小覆盖子串
        # 如果一直没有更新过length，说明没有符合情况的最小子串，返回空string，反之返回最小子串
        result = "" if length == float('inf') else s[start: start + length]

        return result


class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        """
        Time O(n)
        Space O(n)
        同样的逻辑，区别在于我们更新最小substring的时候，直接记录当前的最短string，不需要用一个index记录起始位置。
        """
        window = defaultdict(int)
        need = defaultdict(int)

        for c in t:
            need[c] += 1

        right = 0
        left = 0
        length = float('inf')
        valid = 0
        res = ""

        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                # 区别在这里
                if right - left < length:
                    # 直接记录当前最短substring
                    res = s[left: right]
                    length = right - left
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return res


s = Solution2()
print(s.minWindow(s="ADOBECODEBANC", t="ABC"))
