from collections import Counter
import heapq
from typing import List


class Solution:
    def get_median(self, max_heap, min_heap, k):
        return -max_heap[0] if k & 1 else (min_heap[0] - max_heap[0]) / 2

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        Time O(n * log(k))
        Space O(n)
        对于n个数，每次我们需要log(n)操作加入或者弹出优先列队。
        此题灵感来源于295，依旧是构造大顶堆和小顶堆来找中位数。如何判断两个堆是否平衡，这里我们用一个参数balance来track
        count of valid elements in both heaps是否平衡。
        如果当前要移动出去的数字在大顶堆内，或者当前加入的新数字去小顶堆，此时 balance -= 1。
        如果当前要移动出去的数字在小顶堆内，或者当前加入的新数字去大顶堆，此时 balance += 1。
        balance对应三种状态：
        balance = 0: 两个堆达到平衡，不需要什么操作。
        balance < 0: 大顶堆需要更多的元素。弹出小顶堆最小值去加入进大顶堆。
        balance > 0: 小顶堆需要更多的元素。弹出大顶堆最大值去加入进小顶堆。
        对于要移除的数字，我们采用lazy removal的方式，也就是我们持续记录要移除的数字的频率。
        如果大顶堆的最大值在要移除的字典内，说明大顶堆头结点需要改变也就是此时的中位数有变化，移除大顶堆头结点。
        同理对于小顶堆。但是如果要移除数不在两个堆的头结点，我们什么操作都不执行，留在堆内，
        因为前面判断过是否平衡的操作，即使留在堆内，也不影响中位数的选择。
        """
        max_heap = []  # store the smaller half of the numbers
        min_heap = []  # store the larger half of the number
        to_remove = Counter()  # {int to remove: count}
        # 前k个先进大顶堆
        for i in range(k):
            heapq.heappush(max_heap, -nums[i])

        # 这里同295，大顶堆永远大于等于1个数小顶堆
        # 持续弹出一半或者一半-1个大顶堆进小顶堆，分成两个部分
        for i in range(k // 2):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        # 提取中位数
        res = [self.get_median(max_heap, min_heap, k)]

        for i in range(k, len(nums)):
            # 平衡参数
            balance = 0
            # 出去的数
            out_num = nums[i - k]
            # 进来的数
            in_num = nums[i]
            # 记录出去的数的频率
            to_remove[out_num] += 1

            # 更新平衡参数通过查看移除的数在那一边
            balance += -1 if max_heap and out_num <= -max_heap[0] else 1

            # 如果进来的数在大顶堆
            if max_heap and in_num <= -max_heap[0]:
                heapq.heappush(max_heap, -in_num)
                balance += 1
            # 如果进来的在小顶堆
            else:
                heapq.heappush(min_heap, in_num)
                balance -= 1

            # 大顶堆多于小顶堆
            if balance > 0:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            # 相反
            if balance < 0:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

            # 查看移除的数在哪一边
            while max_heap and to_remove[-max_heap[0]]:
                to_remove[-heapq.heappop(max_heap)] -= 1
            while min_heap and to_remove[min_heap[0]]:
                to_remove[heapq.heappop(min_heap)] -= 1

            # 提取新的中位数
            res.append(self.get_median(max_heap, min_heap, k))

        return res


s = Solution()
print(s.medianSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
