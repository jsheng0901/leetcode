from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        Time O(nlog(n))
        Space O(n)
        贪心思路 + 排序，每一个人都达到局部最优，最终达到全局最优。每个人局部最优的方式是找到两个城市差值并排序从小到大。
        因为选择A还是B的理由是因为差值底则选择哪一个。
        """
        total = 0
        n = len(costs) // 2
        # 对选择A而不是B的差值进行排序，也就是A - B 越小越往前
        costs = sorted(costs, key=lambda x: x[0] - x[1])
        # 前一半去A城市，后一半去B城市
        for i in range(len(costs)):
            if i < n:
                total += costs[i][0]
            else:
                total += costs[i][1]

        return total


s = Solution()
print(s.twoCitySchedCost(costs=[[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]))
