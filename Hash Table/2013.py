import collections
from typing import List


class DetectSquares:

    def __init__(self):
        """
        Time O(n)
        Space O(n)
        核心思想是统计每个点出现的频率，然后计算正方形corner对角线的点十分存在，如果存在，找其它两个角的点存在的频率，相乘即为最终答案个数。
        """
        # 统计每个点出现的频率
        self.points = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        """
        Time O(1)
        """
        # 更新点出现的频率
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        """
        square_count = 0
        x1, y1 = point
        # 找对角线的那个corner点，因为这里是正方形，而不是长方形
        for (x2, y2), n in self.points.items():
            x_dist, y_dist = abs(x1 - x2), abs(y1 - y2)
            # 只有边长相等并且对角线的点不是同一个轴上面的点才行
            if x_dist == y_dist and x_dist > 0:
                # 其它两个corner点
                corner1 = (x1, y2)
                corner2 = (x2, y1)
                # 如果同时存在，计算出现的频率乘积
                if corner1 in self.points and corner2 in self.points:
                    square_count += n * self.points[corner1] * self.points[corner2]

        return square_count


obj = DetectSquares()
obj.add([3, 10])
obj.add([11, 2])
obj.add([3, 2])
print(obj.count([11, 10]))
print(obj.count([14, 8]))
obj.add([11, 2])
print(obj.count([11, 10]))

