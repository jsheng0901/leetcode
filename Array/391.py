from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        Time O(n)
        Space O(1)
        完美矩形，需要从「面积」和「顶点」两个角度来处理。
        面积角度：矩形区域的面积等于所有矩形的面积之和，
        顶点角度：矩形区域四角的顶点只能出现一次，且其余顶点的出现次数只能是两次或四次。
        """
        final_x1, final_y1 = float('inf'), float('inf')
        final_x2, final_y2 = float('-inf'), float('-inf')

        points = set()
        actual_area = 0
        for rect in rectangles:
            x1, y1, x2, y2 = rect
            # 计算完美矩形的理论顶点坐标
            final_x1 = min(final_x1, x1)
            final_y1 = min(final_y1, y1)
            final_x2 = max(final_x2, x2)
            final_y2 = max(final_y2, y2)
            # 累加小矩形的面积
            actual_area += (x2 - x1) * (y2 - y1)
            # 记录最终形成的图形中的顶点
            p1 = (x1, y1)
            p2 = (x1, y2)
            p3 = (x2, y1)
            p4 = (x2, y2)
            # 保证偶数次出现的点最终会被移除，奇数次出现的点留下来，也就是最终的四个大矩形的顶点
            for p in [p1, p2, p3, p4]:
                # 如果出现过就移除
                if p in points:
                    points.remove(p)
                # 如果没有出现过就加入
                else:
                    points.add(p)

        # 判断面积是否相同
        expected_area = (final_x2 - final_x1) * (final_y2 - final_y1)
        if actual_area != expected_area:
            return False

        # 判断最终留下的顶点个数是否为 4
        if len(points) != 4:
            return False

        # 判断留下的 4 个顶点是否是完美矩形的顶点
        if (final_x1, final_y1) not in points:
            return False
        if (final_x1, final_y2) not in points:
            return False
        if (final_x2, final_y1) not in points:
            return False
        if (final_x2, final_y2) not in points:
            return False

        # 面积和顶点都对应，说明矩形符合题意
        return True


s = Solution()
print(s.isRectangleCover(rectangles=[[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]))
