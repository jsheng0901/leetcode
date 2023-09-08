from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.total = 0

    def traversal(self, id, manager_to_subordinates, informTime, cur_time):
        # 记录当前节点传给下一个节点的时间
        cur_time += informTime[id]
        # 遇到叶子节点开始更新最大值，统计最大总时间
        if id not in manager_to_subordinates:
            self.total = max(self.total, cur_time)
            return
        # 对每个孩子节点递归
        for child in manager_to_subordinates[id]:
            self.traversal(child, manager_to_subordinates, informTime, cur_time)

        return

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        先构建manager到employee ID的dictionary，表示树的关系。从头到尾开始dfs遍历整个树，找到最大的路径和及最终的结果。
        """
        # 构建字典表示的树
        manager_to_subordinates = defaultdict(list)
        for index, value in enumerate(manager):
            manager_to_subordinates[value].append(index)

        self.traversal(headID, manager_to_subordinates, informTime, 0)

        return self.total


n = 11
headID = 4
manager = [5, 9, 6, 10, -1, 8, 9, 1, 9, 3, 4]
informTime = [0, 213, 0, 253, 686, 170, 975, 0, 261, 309, 337]
s = Solution()
print(s.numOfMinutes(n=n, headID=headID, manager=manager, informTime=informTime))
