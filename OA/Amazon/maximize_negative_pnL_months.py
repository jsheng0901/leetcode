# 2024-05-02
# You are analyzing the market trends of Amazon stocks. An AWS financial service model returned an array of integers,
# PnL (Profit and Loss), for your portfolio representing that in the ith month, you will either gain or lose PnL[i].
# All reported PnL values are positive, representing gains.
#
# As part of the analysis, you will perform the following operation on the PnL array any number of times:
#
# Choose any month (0 ≤ i < n) and multiply PnL[i] by -1 Find the maximum number of months you can afford to face a
# loss, i.e., have a negative PnL, such that the cumulative PnL for each of the n months remains strictly positive
# i.e. remains greater than 0.
#
# Note: The cumulative PnL for the ith month is defined as the sum of PnL from the starting month up to the ith
# month. For example, the cumulative PnL for the PnL = [3, -2, 5, -6, 1] is [3, 1, 6, 0, 1].
#
# Function Description
#
# Complete the function maximizeNegativePnLMonths in the editor.
#
# maximizeNegativePnLMonths has the following parameter:
#
# int[] PnL: an array of integers representing the Profit and Loss for each month
# Returns
#
# int: the maximum number of months with a negative PnL such that the cumulative PnL remains positive
from typing import List
import heapq


class Solution1:
    def check_same(self, PnL):
        first = PnL[0]
        for val in PnL:
            if val != first:
                return False

        return True

    def maximizeNegativePnLMonths(self, PnL: List[int]) -> int:
        """
        Time O(n + n * log(n))
        Space O(n)
        优先列队存储最小的数字先，贪心思想，每次先移除最小的那个数字看看是否符合要求，符合要求就继续移除下一个最小的数字。这里难点在一直更新
        前缀和数组，并且不需要重复计算。同时还需要满足每次更新后，所有的前缀和位置的数都是大于0的。
        """
        # 特殊情况，全都一样数字，直接返回除数
        if self.check_same(PnL):
            return len(PnL) // 2

        total_sum = [0] * len(PnL)
        total_sum[0] = PnL[0]
        # 计算原始前缀和
        for i in range(1, len(total_sum)):
            total_sum[i] = total_sum[i - 1] + PnL[i]

        # 所有数字从小到大进列队同时带index
        pq = []
        for idx, val in enumerate(PnL):
            heapq.heappush(pq, (val, idx))

        # 遍历整个优先列队
        res = 0
        while pq:
            val, idx = heapq.heappop(pq)
            count = 0
            # 找到当前最小数字的index和值
            for j in range(idx, len(total_sum)):
                # 新的前缀和
                new_sum = total_sum[j] - 2 * val
                # 如果大于0，符合要求，就更新当前位置的前缀和，同时计数器 +1
                if new_sum > 0:
                    count += 1
                    total_sum[j] = new_sum
                else:
                    break
            # 如果后面所有位置的前缀和都满足要求，计数器相等则说明此操作合规，结果 +1
            if count == len(total_sum) - idx:
                res += 1

        return res


class Solution2:
    def backtracking(self, PnL, index, cur_sum, num_neg_month):
        # 走到底了，直接返回当前负数月份
        if index == len(PnL):
            return num_neg_month

        # 当前节点返回值初始化
        max_num_neg_month = float('-inf')
        # 情况1，保存正数
        tmp1 = self.backtracking(PnL, index + 1, cur_sum + PnL[index], num_neg_month)
        # 更新结果
        max_num_neg_month = max(tmp1, max_num_neg_month)
        # 情况2，取负数，这里有个减枝，先判断一下能否保证是positive的，可以则继续下一个点
        if cur_sum - PnL[index] > 0:
            tmp2 = self.backtracking(PnL, index + 1, cur_sum - PnL[index], num_neg_month + 1)
            max_num_neg_month = max(tmp2, max_num_neg_month)

        # 返回当前节点最大的负数操作个数
        return max_num_neg_month

    def maximizeNegativePnLMonths(self, PnL: List[int]) -> int:
        """
        Time O(2^n)
        Space O(n)
        回溯暴力搜索，每个位置两种情况，要么保存正数，要么负数，分布计算出所有情况，对比哪一种负数个数最大，返回结果。
        """
        return self.backtracking(PnL, 0, 0, 0)


s = Solution2()
print(s.maximizeNegativePnLMonths(PnL=[5, 3, 1, 2]))
print(s.maximizeNegativePnLMonths(PnL=[1, 1, 1, 1, 1]))
print(s.maximizeNegativePnLMonths(PnL=[5, 2, 3, 5, 2, 3]))
print(s.maximizeNegativePnLMonths(PnL=[5, 4, 2, 4, 5]))
