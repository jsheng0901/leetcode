# 2024-05-16
# Amazon uses small, Roomba-shaped robots, called "Drives". They deliver large stacks of products to human workers by
# following set paths around the warehouse.
#
# The warehouse can be represented in the form of a cartesian plane, where robots are located at integral points of the
# form (x, y). When a product is to be delivered to some point (i, j), the nearest robot is sought and chosen.
# Thus, if a robot is surrounded by other robots nearby, it will seldom be chosen for work. More formally,
# a robot is said to be idle if it has a robot located above, below, left, and right of it. It is guaranteed that no two
# robots are at the same location.
#
# Given the locations of n robots, find the number of idle robots.
#
# Function Description
#
# Complete the function numIdleDrives in the editor below.
#
# numIdleDrives has the following parameters:
#
# int x[n]: x[i] is the x-coordinate of the ith robot, where 0 ≤ i < n.
# int y[n]: y[i] is the y-coordinate of the ith robot, where 0 ≤ i < n.
# Returns
#
# int: the number of idle robots
from typing import List
from collections import defaultdict


class Solution1:
    def numIdleDrives(self, x: List[int], y: List[int]) -> int:
        """
        Time O(n * n * log(n))
        Space O(n)
        遍历每个点，找出x，y对应的同一个轴上面的其它的点，并且排序。之后在遍历一次所有点，如果有一个方向排在第一个或者最后一个，
        那就不可能是idle driver。计算不是的个数，总个数减去不是的个数等于是的个数。
        """
        # x轴对应的其它y值的点
        col_ranges = {}
        # y轴对应的其它x值的点
        row_ranges = {}
        for x_c, y_c in zip(x, y):
            # 记录当前x轴的值对应的其它y轴的点，并排序
            if x_c in col_ranges:
                col_ranges[x_c].append(y_c)
                col_ranges[x_c].sort()
            else:
                col_ranges[x_c] = [y_c]
            # 记录当前y轴的值对应的其它x轴的点，并排序
            if y_c in row_ranges:
                row_ranges[y_c].append(x_c)
                row_ranges[y_c].sort()
            else:
                row_ranges[y_c] = [x_c]

        active_cnt = 0
        for x_c, y_c in zip(x, y):
            # flag标记是否有一个方向在最旁边
            is_active = False
            # 左右两边一个是最旁边
            if x_c == row_ranges[y_c][0] or x_c == row_ranges[y_c][-1]:
                is_active = True
            # 上下有一个是最旁边
            if y_c == col_ranges[x_c][0] or y_c == col_ranges[x_c][-1]:
                is_active = True
            # 满足一个条件即可
            if is_active:
                active_cnt += 1

        # 取反面
        return len(x) - active_cnt


class Solution2:
    def numIdleDrives(self, x: List[int], y: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        遍历每个点，找出x，y对应的同一个轴上面的其它的点，其实这里我们并不需要对整个数组排序，完全可以只需要维护最大值最小值即可，因为我们后面
        找的是反例，所以只需要知道当前点是不是最旁边的两个点即可，也就说我们只需要维护一个数组记录最大值最小值就行了。
        之后同思路一，在遍历一次所有点，如果有一个方向排在第一个或者最后一个也就是最大或者最小值，那就不可能是idle driver。
        计算不是的个数，总个数减去不是的个数等于是的个数。
        """
        col_ranges = defaultdict(list)
        row_ranges = defaultdict(list)
        for x_c, y_c in zip(x, y):
            # 这里是和思路1最主要不一样的地方，我们维护当前x轴对应的y值的两个最值即可
            if x_c in col_ranges:
                col_ranges[x_c][0] = min(col_ranges[x_c][0], y_c)
                col_ranges[x_c][1] = max(col_ranges[x_c][1], y_c)
            else:
                col_ranges[x_c].append(y_c)
                col_ranges[x_c].append(y_c)
            # 同上，我们维护当前y轴对应的x值的两个最值即可
            if y_c in row_ranges:
                row_ranges[y_c][0] = min(row_ranges[y_c][0], x_c)
                row_ranges[y_c][1] = max(row_ranges[y_c][1], x_c)
            else:
                row_ranges[y_c].append(x_c)
                row_ranges[y_c].append(x_c)

        # 其它同思路1
        active_cnt = 0
        for x_c, y_c in zip(x, y):
            is_active = False
            if x_c == row_ranges[y_c][0] or x_c == row_ranges[y_c][-1]:
                is_active = True
            if y_c == col_ranges[x_c][0] or y_c == col_ranges[x_c][-1]:
                is_active = True
            if is_active:
                active_cnt += 1

        return len(x) - active_cnt


s = Solution2()
print(s.numIdleDrives(x=[0, 0, 0, 0, 0, 1, 1, 1, 2, -1, -1, -2, -1], y=[-1, 0, 1, 2, -2, 0, 1, -1, 0, 1, -1, 0, 0]))
print(s.numIdleDrives(x=[1, 1, 1, 2, 2, 2, 2, 3, 3, 3], y=[1, 2, 3, 1, 2, 3, 5, 1, 2, 3]))
