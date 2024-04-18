from collections import defaultdict
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        """
        Time O(n^2)
        Space O(n)
        记录所有y轴对应的x值，遍历所有y轴的组合，找到有交集的x轴的值，至少2个以上，再遍历所有交集里面的组合，找到最小面积。
        因为当有两个公用的y轴的时候，至少要有两个公用的x轴的值才能组合成长方形。
        """
        # 找到所有的y对应的x的值的组合
        y_to_x = defaultdict(set)
        for point in points:
            x, y = point[0], point[1]
            y_to_x[y].add(x)

        all_y = list(y_to_x.keys())
        min_area = float('inf')
        # 遍历所有y的组合
        for i in range(len(all_y)):
            y1 = all_y[i]
            for j in range(i + 1, len(all_y)):
                y2 = all_y[j]
                # 找到组合里面x轴的交集
                interesction_x = list(y_to_x[y1].intersection(y_to_x[y2]))
                # 少于2个都不可能组合成长方形
                if len(interesction_x) < 2:
                    continue
                else:
                    # 遍历所有x的组合
                    for k in range(len(interesction_x)):
                        x1 = interesction_x[k]
                        for l in range(k + 1, len(interesction_x)):
                            x2 = interesction_x[l]
                            # 计算面积
                            area = abs(y1 - y2) * abs(x1 - x2)
                            # 更新最小面积
                            min_area = min(min_area, area)

        # 如果没有最小面积，说明不可能组合成长方形，返回0
        return 0 if min_area == float('inf') else min_area


s = Solution()
print(s.minAreaRect(points=[[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]))
