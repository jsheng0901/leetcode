# 2024-05-12
# New Year's Day is around the corner and Amazon is having a sale. They have a list of items they are considering but
# they may need to remove some of them. Determine the minimum number of items to remove from an array of prices so
# that the sum of prices of any k items does not exceed a threshold.
#
# Note: If the number of items in the list is less than k, then there is no need to remove any more items.
#
# Function Description
#
# Complete the function reduceGifts in the editor.
#
# reduceGifts has the following parameters:
#
# 1. int prices[n]: the prices of each item
# 2. int k: the number of items to sum
# 3. int threshold: the maximum price of k items
# Returns
#
# int: the minimum number of items to remove
from typing import List


class Solution:
    def reduceGifts(self, prices: List[int], k: int, threshold: int) -> int:
        """
        Time O(n * log(n) + (n - k + 1) * k)
        Space O(1)
        先sort一下，从大到小。计算前k个数的和，如果超过threshold，说明要丢掉一个，贪心的思想，先丢掉最大的，如果丢一个最大的都不行，那么就
        继续丢第二个最大的数，直到前k个数的和小于threshold，或者剩下的数的个数少于k个数。所以我们第二部分最多遍历 n - k + 1 个数。每个数
        需要计算k个数的和。
        """
        # 从大到小排序
        prices.sort(reverse=True)

        # 从第一个数最大的开始遍历
        i = 0
        while i < len(prices):
            # 如果剩下的少于k，直接返回当前移除的数，就是i
            if len(prices) - i < k:
                return i

            # 计算当前最大的k个数的和
            cur_sum = sum(prices[i: i + k])
            # 如果小于等于threshold，说明已经符合要求，直接返回i
            if cur_sum <= threshold:
                return i

            # 不满足条件，继续移除数
            i += 1

        return i


s = Solution()
print(s.reduceGifts(prices=[3, 2, 1, 4, 6, 5], k=3, threshold=14))
print(s.reduceGifts(prices=[9, 6, 7, 2, 7, 2], k=2, threshold=13))
print(s.reduceGifts(prices=[9, 6, 3, 2, 9, 10, 10, 11], k=4, threshold=1))
