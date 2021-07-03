class Solution:
    def findMinArrowShots(self, points: [[int]]) -> int:
        """
        time: O(nlogn), space: O(1)
        局部最优：当气球出现重叠，一起射，所用弓箭最少。全局最优：把所有气球射爆所用弓箭最少
        :param points:
        :return:
        """
        if len(points) == 0:
            return 0
        # 先排序，按照第一个大小排序，然后从左向右遍历
        points.sort(key=lambda x: x[0])

        result = 1

        for i in range(1, len(points)):
            if points[i][0] <= points[i - 1][1]:  # 当前和前一个有交集 挨在一起也可以
                points[i][1] = min(points[i][1], points[i - 1][1])  # 更新当前这个右边界，为最小右边界
            else:
                result += 1  # 没有交集，所以要另外一个箭

        return result


s = Solution()
print(s.findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))
