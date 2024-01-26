from collections import defaultdict
from typing import List


class Solution:
    def backtracking(self, start_index, balance_list):
        # 回溯模板写法，判断当前节点状态放在开头
        # 当前节点如果已经是0 balance，则不需要继续判断直接跳过此index
        while start_index < len(balance_list) and balance_list[start_index] == 0:
            start_index += 1

        # 走到最后的index了，直接返回0，因为是下一个节点判断当前状态，所以是等于 len(balance_list)
        if start_index == len(balance_list):
            return 0

        # 得到所有子节点的返回值，取最小值返回，用来记录子节点放回结果
        res = float('inf')
        # 遍历当前节点的下一个节点到最后所有节点，这里和一般的回溯不一样的地方在于，不是从当前节点开始loop而且当前节点的下一个节点开始loop
        for i in range(start_index + 1, len(balance_list)):
            # 如果当前节点和下一个节点符号相反，也就是要进行一次交易，才进行回溯
            if balance_list[i] * balance_list[start_index] < 0:
                # 下一个节点的值update
                balance_list[i] += balance_list[start_index]
                # 进入下一个回溯，同时记录最小返回值
                res = min(res, 1 + self.backtracking(start_index + 1, balance_list))
                # 离开当前节点时候，回溯下一个节点的赋值
                balance_list[i] -= balance_list[start_index]

        return res

    def minTransfers(self, transactions: List[List[int]]) -> int:
        """
        Time O((n - 1)!)
        Space O(n)
        首先我们构建一个list来表达每个人最后的balance。然后我们需要找到一条path来让所有balance都变成0，并且距离最短。
        用回溯的方法遍历所有可能的组合，最后选出路径最短的path。详细见注释。
        """
        # 构建balance map 表示每个人给完前后还剩多少钱
        balance_map = defaultdict(int)
        for start, destination, amount in transactions:
            balance_map[start] -= amount
            balance_map[destination] += amount

        # 转化成list，对于已经是0的balance我们不需要任何操作，直接过滤掉
        balance_list = [balance for balance in balance_map.values() if balance != 0]

        return self.backtracking(0, balance_list)


s = Solution()
print(s.minTransfers(transactions=[[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]))
