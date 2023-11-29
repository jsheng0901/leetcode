import collections
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        Time O(n)
        Space O(n)
        转化为找到一个 i - j 的区间内sum大于等于k，并且长度最小。
        前缀和统计到每个index的总和。维护一个单调递增列队记录前缀和从左到右，列队头是最小值。每次check列对头是否和当前总和差值大于等于k，
        及是否是合理的 i - j区间，如果是我们更新长度，并弹出列对头，因为是最小值，所以不会再有更小的值满足差值情况。
        所以可以往下一个列对头查看等同于缩小窗口区间的left指针。
        """
        # 构建前缀和
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)

        deque = collections.deque()
        result = float('inf')
        # 遍历前缀和
        for i, sum_ in enumerate(pre):
            # 如果列队尾的元素大于当前前缀和，说明不是单调递增，需要弹出此时的列队尾
            while deque and deque[-1][1] >= sum_:
                deque.pop()
            # 如果列队头到当前和的区间内满足大于等于k，则说明找到一个合理区间，统计长度，并弹出列队头
            while deque and sum_ - deque[0][1] >= k:
                result = min(i - deque[0][0], result)
                deque.popleft()

            # 添加当前index和前缀和进列队
            deque.append([i, sum_])

        # 如果结果没有更新过说明没有符合情况的和，返回 -1
        return result if result != float('inf') else -1


s = Solution()
print(s.shortestSubarray(nums=[2, -1, 2], k=3))
print(s.shortestSubarray(nums=[1, 2], k=4))
print(s.shortestSubarray(nums=[1], k=1))
print(s.shortestSubarray(nums=[84, -37, 32, 40, 95], k=167))
print(s.shortestSubarray(nums=[56, -21, 56, 35, -9], k=61))
print(s.shortestSubarray(nums=[-28, 81, -20, 28, -29], k=89))
print(s.shortestSubarray(nums=[77, 19, 35, 10, -14], k=19))
