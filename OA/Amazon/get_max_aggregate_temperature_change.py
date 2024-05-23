# 2024-05-16
# Question:
# Alexa is Amazon's virtual AI assistant. It makes it easy to set up your Alexa-enabled devices, listen to music,
# get weather updates, and much more. The team is working on a new feature that evaluates the aggregate temperature
# change for a period based on the changes in temperature of previous and upcoming days.
#
# Taking the change in temperature data of n days, the aggregate temperature change evaluated on the ith day is the
# maximum of the sum of the changes in temperatures until the ith day, and the sum of the change in temperatures in the
# next (n - i) days, with the ith day temperature change included in both.
#
# Given the temperature data of n days, find the maximum aggregate temperature change evaluated among all the days.
#
# Function Description
#
# Complete the function getMaxAggregateTemperatureChange in the editor.
#
# getMaxAggregateTemperatureChange has the following parameter:
#
# int tempChange[n]: the temperature change data of n days
# Returns
#
# long: the maximum aggregate temperature change
from typing import List


class Solution1:
    def getMaxAggregateTemperatureChange(self, tempChange: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        前缀和思路，同2256
        """
        pre_sum = [0] * (len(tempChange) + 1)
        for i in range(1, len(pre_sum)):
            pre_sum[i] = pre_sum[i - 1] + tempChange[i - 1]

        max_change = float('-inf')
        for i in range(len(tempChange)):
            first = pre_sum[i + 1]
            second = pre_sum[-1] - pre_sum[i]
            max_change = max(max_change, max(first, second))

        return max_change


class Solution2:
    def getMaxAggregateTemperatureChange(self, tempChange: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        前缀和思路，同2256
        """
        total_sum = sum(tempChange)
        cur_sum = 0

        max_change = float('-inf')
        for i in range(len(tempChange)):
            pre_sum = cur_sum
            cur_sum += tempChange[i]
            second = total_sum - pre_sum
            max_change = max(max_change, max(cur_sum, second))

        return max_change


s = Solution2()
print(s.getMaxAggregateTemperatureChange(tempChange=[6, -2, 5]))
print(s.getMaxAggregateTemperatureChange(tempChange=[-1, 2, 3]))
