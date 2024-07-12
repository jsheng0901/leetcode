import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        Time O(k * (n * log(n) + n * log(n)))
        Space O(n)
        从profit的角度思考，找最大的profit，
        直到当前的 capital 满足小于等于w的情况，当前profit一定是w下最大的profit。不符合条件的 capital，
        重新加入回去大顶堆。直到k此用完，此方法会超时，因为有可能符合要求的capital在最后面，每次我们都需要弹出前面所有capital然后加入回去，
        这样的话相当费时间。
        """
        group = []
        # 把profit从大到小和capital一起加入大顶堆
        for profit, cap in zip(profits, capital):
            heapq.heappush(group, (-profit, cap))

        while k > 0 and group:
            tmp = []
            cur_profit, cur_cap = heapq.heappop(group)
            # 找到当前最大profit并符合capital的数
            while group and cur_cap > w:
                # 弹出所有不符合的情况，并记录进一个数组
                tmp.append((cur_profit, cur_cap))
                cur_profit, cur_cap = heapq.heappop(group)

            # 如果当前找到的符合条件，更新capital和次数
            if cur_cap <= w:
                w -= cur_profit
                k -= 1

            # 把不符合的加入回大顶堆
            while tmp:
                heapq.heappush(group, tmp.pop())

        return w


class Solution2:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        Time O(n * log(n))
        Space O(n)
        把所有的capital和profit放进一个数组，同时从小到大sort capital，因为我们的起步capital是最小的，所以直接从小开始遍历所有capital，
        并统计目前为止所有小于当下capital的profit，直到capital大于当前我们的起步capital，弹出大顶堆的堆顶，一定是最大的profit，更新当前
        capital，此时对于下一个profit我们并不需要从头开始遍历所有capital，继续遍历刚刚走到的capital，因为此时的起步capital已经更大了，
        最大的profit一定在大顶堆里面或者在之后的capital数组内。直到用完所有k此选择。
        """
        group = []
        pq = []
        # group起来一起放进数组
        for profit, cap in zip(profits, capital):
            group.append((cap, profit))

        # 从小打到sort capital
        group.sort(key=lambda x: x[0])
        i = 0
        while k > 0:
            # 当前 capital 小于等于w的时候，记录profit
            while i < len(group) and group[i][0] <= w:
                # 记录进大顶堆
                heapq.heappush(pq, -group[i][1])
                i += 1

            # 如果是空的列队
            if not pq:
                # 说明没有符合题意的capital了，直接结束循环
                break

            # 更新当前的capital，大顶堆是负数，用减法
            w -= heapq.heappop(pq)
            # 更新次数
            k -= 1

        return w


s = Solution2()
print(s.findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]))
print(s.findMaximizedCapital(k=3, w=0, profits=[1, 2, 3], capital=[0, 1, 2]))
print(s.findMaximizedCapital(k=1, w=0, profits=[1, 2, 3], capital=[1, 1, 2]))
