# 2024-05-14
# Amazon has multiple delivery centers and delivery warehouses all over the world! The world is represented by a number
# line from -109 to 109. There are n delivery centers, the ith one at location center[i]. A location x is called a
# suitable location for a warehouse if it is possible to bring all the products to that point by traveling a distance
# of no more than d. At any one time, products can be brought from one delivery center and placed at point x.
# Given the positions of n delivery centers, calculate the number of suitable locations in the world.
# That is, calculate the number of points x on the number line (-109 ≤ x ≤ 109) where the travel distance required to
# bring all the products to that point is less than or equal to d.
#
# Note: The distance between point x and center[i] is |x - center[i]|, their absolute difference.
from typing import List


class Solution:
    def get_distance(self, x, center):
        dist = 0

        for c in center:
            dist += 2 * abs(c- x)

        return dist

    def left_bound(self, center, left, right, d):

        while left <= right:
            mid = left + (right - left) // 2
            # 计算到center的距离和，判断和要求distance的距离
            dist = self.get_distance(mid, center)
            # 这里当小于要求距离的时候，我们不是要逼近target值，而是要找最远离的左边界点，也就是最远离target值的符合要求的点，
            # 所以小于等于的时候，我们都是缩放右指针
            if dist < d:
                right = mid - 1
            elif dist == d:
                right = mid - 1
            elif dist > d:
                left = mid + 1

        return left

    def right_bound(self, center, left, right, d):

        while left <= right:
            mid = left + (right - left) // 2
            dist = self.get_distance(mid, center)
            # 同左边的写法，这里找的是最原理的右边界的点
            if dist < d:
                left = mid + 1
            elif dist == d:
                left = mid + 1
            elif dist > d:
                right = mid - 1

        return right

    def numberOfSuitableLocations(self, center: List[int], d: int) -> int:
        """
        Time O(log(n))
        Space O(1)
        二分法查找，在整个坐标轴上面找符合distance要求的左边界和右边界，两个边界里面的点都是符合要求的点。
        这里需要注意的是，左边界的和右边界有点不一样，详细见注释。
        """
        left = -10 ** 9
        right = 10 ** 9

        # 左边界
        left_bound = self.left_bound(center, left, right, d)
        # 如果左边界不存在，也就是左边界无限接近右边界 while loop后，则说明没有这个点存在，直接返回0
        if left_bound >= 10 ** 9:
            return 0
        # 右边界，如果左边界存在，则一定有右边界，最差情况右边界就是左边界自己
        right_bound = self.right_bound(center, left, right, d)

        # 返回边界里面点的个数
        return right_bound - left_bound + 1


s = Solution()
print(s.numberOfSuitableLocations(center=[-2, 1, 0], d=8))
print(s.numberOfSuitableLocations(center=[2, 0, 3, -4], d=22))
print(s.numberOfSuitableLocations(center=[-3, 2, 2], d=8))
