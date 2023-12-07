import heapq
import random
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time O(n log(k))    k is top element size in heapq
        Space O(n + k)      map + heap
        first count frequency takes O(n), then build a min heap for each element, each pop and push takes log(n)
        here we use build in heap, then transfer to list.
        """
        # nums 中的元素 -> 该元素出现的频率
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        # 列队顶就是最小值
        min_heap = []
        # 按照键值对中的值（元素出现频率）从小到大排序
        for key, val in freq.items():
            heapq.heappush(min_heap, (val, key))
            if len(min_heap) > k:
                # 弹出最小元素，维护队列内是 k 个频率最大的元素
                heapq.heappop(min_heap)

        top_numbers = [el[1] for el in min_heap]

        return top_numbers


class Solution2:
    def __init__(self):
        self.unique = None

    def partition(self, left, right, pivot_index, value_to_freq):
        # partition function用于把pivot index放到正确的位置，也就是排序好pivot index的位置
        pivot_freq = value_to_freq[self.unique[pivot_index]]
        # 1. Move the pivot to end
        self.unique[pivot_index], self.unique[right] = self.unique[right], self.unique[pivot_index]

        # 2. Move all less frequent elements to the left
        # 此逻辑相当于遇到大于自己的不动，让一个指针停在大于这里用来找到下一个小于的数进行交换，遇到小于自己的要移动到左边去，所以和
        # 大于自己的那个指针进行交换，最终把pivot和最后交换完所有小于自己的指针进行交换。则左边都是小于自己的数，右边都是大于自己的数。
        store_index = left
        for i in range(left, right):
            if value_to_freq[self.unique[i]] < pivot_freq:
                self.unique[store_index], self.unique[i] = self.unique[i], self.unique[store_index]
                store_index += 1

        # 3. Move the pivot to its final place
        self.unique[right], self.unique[store_index] = self.unique[store_index], self.unique[right]
        # 返回pivot index处于的正确位置
        return store_index

    def quick_select(self, left, right, k_smallest, value_to_freq):
        # 当数组只剩下一个数的时候，结束递归
        if left == right:
            return
        # 随机选择一个作为 pivot index
        pivot_index = random.randint(left, right)
        # 找到排序结束后 pivot index 的正确位置
        pivot_index = self.partition(left, right, pivot_index, value_to_freq)

        # 如果刚好是我们要找的位置在排序后的list里面，直接结束
        if k_smallest == pivot_index:
            return
        # 要找的位置当前位置的左边，则从新排序左边
        elif k_smallest < pivot_index:
            self.quick_select(left, pivot_index - 1, k_smallest, value_to_freq)
        # 要找的位置当前位置的右边，则从新排序右边
        else:
            self.quick_select(pivot_index + 1, right, k_smallest, value_to_freq)

        return

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time O(n)
        Space O(n)
        利用quick select的方法，我们算出频率后，找到一个点，把小于他频率的移到左边，大于等于他频率的移到右边，最终我们需要找的是一个index，
        满足 n - k == index，转化 k 个最大变成 第 n - k 个最小对应的 index。这里我们并不需要两边都排序，每次只要去一边，所以时间是O(n)。
        ex: pivot index: 2， 多次排序后为 [4, 3, 1, 5, 2]，此时 n - k -> 5 - 3 = 2 等于我们此时的pivot index，
        """
        # nums 中的元素 -> 该元素出现的频率
        value_to_freq = {}
        for i in nums:
            value_to_freq[i] = value_to_freq.get(i, 0) + 1

        # 统计所有keys，不重复的元素
        self.unique = list(value_to_freq.keys())
        n = len(self.unique)
        # 快排
        self.quick_select(0, n - 1, n - k, value_to_freq)
        # 返回最大的几个数
        return self.unique[n - k:]


s = Solution2()
print(s.topKFrequent([1, 1, 1, 2, 2, 4], 2))
