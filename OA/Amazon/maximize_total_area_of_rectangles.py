# 2024-04-07

# Amazon games have introduced a new mathematical game for kids. You will be given n sticks and the player is
# required to form rectangles from those sticks.
#
# Formally, given an array of n integers representing the lengths of the sticks, you are required to create
# rectangles using those sticks. Note that a particular stick can be used in at most one rectangle and in order to
# create a rectangle we must have exactly two pairs of sticks with the same lengths. For example, you can create a
# rectangle using sticks of lengths [2, 2, 5, 5] and [4, 4, 4, 4] but not with [3, 3, 5, 8]. The goal of the game is
# to maximize the total sum of areas of all the rectangles formed.
#
# In order to make the game more interesting, we are allowed to reduce any integer by at most 1. Given the array
# sideLengths, representing the length of the sticks, find the maximum sum of areas of rectangles that can be formed
# such that each element of the array can be used as length or breadth of at most one rectangle, and you are allowed
# to decrease any integer by at most 1. Since this number can be quite large, return the answer modulo 10^9+7.
#
# Note: It is not a requirement that all side lengths be used. Also, a modulo b here represents the remainder
# obtained when an integer an is divided by an integer b.
#
# Function Description
#
# Complete the function getMaxTotalArea in the editor.
#
# getMaxTotalArea has the following parameter(s):
#
# int sideLengths[n]: the side lengths that can be used to form rectangles
# Returns
#
# int: the maximum total area of the rectangles that can be formed, modulo (10^9+7).

import heapq
from typing import List


class Solution1:
    def getMaxTotalArea(self, sideLengths: List[int]) -> int:
        """
        Time O(n * log(n) + n * log(n))
        Space O(n)
        先sort一下，保证遍历的时候从大到小找边长，每条边三种情况：
        1. 可以和下一条边构成一对
        2. 减1后可以和下一条边构成一对
        3. 不能构成一对
        找到所有能构成的边之后，放进大顶堆然后，再一次弹出计算最大面积和。
        """
        # 从大到小排列
        sideLengths.sort(reverse=True)
        # 统计最长的边，大顶堆
        max_heap = []
        i = 0
        max_area = 0
        while i < len(sideLengths) - 1:
            # 情况1，可以和下一条边构成一对
            if sideLengths[i] == sideLengths[i + 1]:
                heapq.heappush(max_heap, -sideLengths[i])
                i += 2
            # 情况2，减1后可以和下一条边构成一对
            elif sideLengths[i] - sideLengths[i + 1] == 1:
                heapq.heappush(max_heap, -(sideLengths[i] - 1))
                i += 2
            # 情况3，不能构成一对，跳过
            else:
                i += 1

        # 依次弹出边长，计算面积和
        while len(max_heap) >= 2:
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)
            max_area += first * second

        return max_area % (10 ** 9 + 7)


class Solution2:
    def getMaxTotalArea(self, sideLengths: List[int]) -> int:
        """
        Time (n * log(n))
        Space O(1)
        从思路1可以看出来，大顶堆存在的意义是保证计算面积的时候是从大到小的弹出两条边，然后计算面积和保证最大。其实sort后每次找到的边一定是
        从大到小的顺序，那么我们完全可以用两个指针来记录每次找到的两组变成，然后计算面积和，同时更新指针。
        """
        # 从大到小排列
        sideLengths.sort(reverse=True)
        i = 0
        max_area = 0
        # 指针1，记录长
        length = 0
        # 指针2，记录宽
        breadth = 0
        while i < len(sideLengths) - 1:
            # 情况1，可以和下一条边构成一对
            if sideLengths[i] == sideLengths[i + 1]:
                # 如果长是空的，指针赋值
                if length == 0:
                    length = sideLengths[i]
                # 如果宽是空的，指针赋值
                elif breadth == 0:
                    breadth = sideLengths[i]
                i += 2
            # 情况2，减1后可以和下一条边构成一对
            elif sideLengths[i] - sideLengths[i + 1] == 1:
                # 如果长是空的，指针赋值
                if length == 0:
                    length = sideLengths[i + 1]
                # 如果宽是空的，指针赋值
                elif breadth == 0:
                    breadth = sideLengths[i + 1]
                i += 2
            # 情况3，不能构成一对，跳过
            else:
                i += 1

            # 在这里更新面积和重新初始化指针的值，当长宽都找到的时候，说明可以计算面积了
            if length != 0 and breadth != 0:
                # 累加面积和
                max_area += length * breadth
                # 重新初始化指针值
                length = 0
                breadth = 0

        return max_area % (10 ** 9 + 7)


s = Solution2()
print(s.getMaxTotalArea(sideLengths=[2, 6, 2, 6, 3, 5]))
print(s.getMaxTotalArea(sideLengths=[2, 3, 3, 4, 6, 8, 8, 6]))
print(s.getMaxTotalArea(sideLengths=[3, 4, 5, 5, 6]))
