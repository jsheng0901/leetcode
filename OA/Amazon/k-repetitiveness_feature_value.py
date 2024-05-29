# 2024-04-16

# The team of machine learning scientists at Amazon wants to improve Amazon's product recommendation system. Based on
# a user's purchase history, the objective is to generate some extensive features that will be given as input to the
# machine learning model. One of the new proposed features is a k-repetitiveness feature whose computation is
# described below.
#
# The purchase history of a user with the products available on Amazon is available in the form of a string
# user_history where the ith character represents the category of the ith product purchased by the user. The length
# of string user_history is n. There is also a given integer k.
#
# The value of the k-repetitiveness feature for the string user_history is defined as the maximum number of
# substrings of the given string such that some product category in that substring appeared at least k times.
#
# Find the value of the k-repetitiveness feature for the given string user_history.
#
# Note: A substring is a continuous subsegment of a string.
#
# Function Description
#
# Complete the function getkRepValue in the editor.
#
# getkRepValue has the following parameters:
#
# String user_history: the interaction history of the user
# int k: the minimum occurrence of a product for a substring to be included in the k-repetitiveness feature
# Returns
#
# An integer denoting the value of the k-repetitiveness feature.
from collections import defaultdict


class Solution1:
    def getkRepValue(self, user_history: str, k: int) -> int:
        n = len(user_history)
        res = 0

        for i in range(n):
            for j in range(i, n):
                sub_string = user_history[i: j + 1]
                freq = defaultdict(int)
                for c in sub_string:
                    freq[c] += 1
                    if freq[c] >= k:
                        res += 1
                        break

        return res


class Solution2:
    def getkRepValue(self, user_history: str, k: int) -> int:
        """
        Time O(n)
        Space O(n)
        滑动窗口思路，参考992，求大于等于k的滑动窗口substring有多少个转化成，total substring - 小于k的substring。
        窗口内一直维护一个符合小于k要求的substring，当等于的时候，开始移动左指针，直到重新符合要求，再计算此时弹出后substring的个数，
        之后继续移动右指针，详细见注释。这里有个公式：一个substring移动指针后有多少个多出来的新的substring等于 right - left + 1个。
        """
        n = len(user_history)
        # 计算总共有多少substring
        total_substring = int((n * (n + 1)) / 2)
        # 统计小于k的情况的个数substring
        opposite_num = 0
        # 标记找到不合理的情况
        valid_flag = False
        # 不合理情况的字符
        valid_char = None
        # 两个指针
        left = 0
        right = 0
        # 窗口内统计频率
        window = defaultdict(int)
        while right < n:
            # 进窗口的字符
            c = user_history[right]
            # 叠加
            window[c] += 1
            # 满足invalid，标记起来
            if window[c] == k:
                valid_flag = True
                valid_char = c
            # 没有invalid，叠加统计substring的个数
            else:
                opposite_num += right - left + 1
            right += 1

            # 当invalid的时候开始移动左指针
            while valid_flag:
                # 弹出的字符
                d = user_history[left]
                # 更新窗口
                window[d] -= 1
                # 移动左指针
                left += 1
                # 满足条件，开始更新
                if d == valid_char:
                    # 左指针移动，计算跳出invalid的状态后，多出来的substring
                    opposite_num += (right - 1) - left + 1
                    # 重新初始化flag
                    valid_flag = False
                    valid_char = None

        # 计算反面，相减
        return total_substring - opposite_num


s = Solution2()
print(s.getkRepValue(user_history="ceccca", k=3))
print(s.getkRepValue(user_history="acaab", k=3))
print(s.getkRepValue(user_history="cecce", k=2))
