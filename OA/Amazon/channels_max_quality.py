# 2024-04-11
# You are given a list of packets of varying sizes and there are n channels.
#
# Each of the n channel must have a single packet Each packet can only be on a single channel The quality of a
# channel is described as the median of the packet sizes on that channel. The total quality is defined as sum of the
# quality of all channels (round to integer in case of float).
#
# Given the packet sizes and num of channels, find the maximum quality.
#
# Function Description
#
# Complete the function calculateMedianSum in the editor.
#
# calculateMedianSum has the following parameters:
#
# int[] packets: an array of integers
# int n: the number of channels
# Returns
#
# int: the sum of the medians of each channel
import math
from typing import List


class Solution:
    def calculateMedianSum(self, packets: List[int], n: int) -> int:
        """
        Time O(n * log(n) + n)
        Space O(1)
        贪心的思想，先sort一遍，要想中位数最大，每次都只放一个数进channel先，直到最后一个channel，全部放进去。
        """
        packets.sort()

        res = 0
        # 从大到小遍历
        for i in range(len(packets) - 1, -1, -1):
            # 多个channel的时候，先放最大数
            if n > 1:
                # 中位数就是自己
                res += packets[i]
                # 更新channel的个数
                n -= 1
            else:
                # 只剩下一个channel后，全部放进去
                # 如果是偶数，取平均数
                if i % 2 == 1:
                    res += (packets[i // 2] + packets[(i // 2) + 1]) / 2
                # 如果是奇数，中位数就是中间那个
                else:
                    res += packets[i // 2]
                # 直接结束遍历
                break

        # 返回结果，这里要round一下
        return math.ceil(res)


s = Solution()
print(s.calculateMedianSum(packets=[1, 2, 3, 4, 5], n=2))
print(s.calculateMedianSum(packets=[5, 2, 2, 1, 5, 3], n=2))
