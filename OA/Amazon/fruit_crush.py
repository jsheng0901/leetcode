# 2024-04-10
# Amazon recently launched a new game, Fruit Crush! In this game, you are allowed to choose two dissimilar fruits and
# crush them. Each type of fruit is represented as an integer in an array. Formally you can choose any two unequal
# integers in the array and delete them.
#
# Given an array fruits of size n, return the minimum possible number of fruits left after the given operation is
# performed any number of times.
#
# Function Description
#
# Complete the function getMinimumFruits in the editor.
#
# getMinimumFruits has the following parameter(s):
#
# int fruits[n]: array of n fruits
# Returns
#
# int: the minimum possible count of fruits left
from typing import List
from collections import Counter
import heapq


class Solution:
    def getMinimumFruits(self, fruits: List[int]) -> int:
        """
        Time O(n * log(n))
        Space O(n)
        计算频率，按照频率的大小从大到小进入大顶堆，每次弹出堆顶的两个元素，同时消除一对，更新频率，如果不等于0，重新插入回去大顶堆，
        直到弹出所有，或者还有一个剩下，返回的是剩下的这个水果的频率不是剩下的个数。一定最终剩下个水果个数是1或者0。
        """
        # 计算水果出现的频率
        freq = Counter(fruits)
        pq = []
        # 进入大顶堆
        for val in freq.values():
            heapq.heappush(pq, -val)

        while len(pq) > 1:
            # 前两个的频率，记得取负数
            front1 = -heapq.heappop(pq)
            front2 = -heapq.heappop(pq)
            # 更新频率
            new_freq_front1 = front1 - 1
            new_freq_front2 = front2 - 1

            # 如果还有水果，则继续加入回去
            if new_freq_front1 != 0:
                heapq.heappush(pq, -new_freq_front1)
            # 同上
            if new_freq_front2 != 0:
                heapq.heappush(pq, -new_freq_front2)

        # 返回结果，记得是频率不是个数
        return -pq[0] if len(pq) == 1 else 0


s = Solution()
print(s.getMinimumFruits(fruits=[1, 2, 5, 6]))
print(s.getMinimumFruits(fruits=[3, 3, 1, 1, 2]))
print(s.getMinimumFruits(fruits=[1, 1, 1, 2, 2, 2, 3, 3]))
print(s.getMinimumFruits(fruits=[1, 1, 1, 1]))
