from collections import defaultdict
from typing import List


class Solution1:
    def get_presum(self, nums):
        pre_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        return pre_sum

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Time O(n + n * d)  d -> range between lower and upper
        Space O(n)
        核心思想利用前缀和高效的计算区间和，我们可以遍历所有前缀和的数，然后在所有的range范围内计算需要的差值，也就是差值是否存在于前缀和数组
        内，然后统计频率，计算出现的个数。但是这里需要遍历整个range里面所有的数，如果range很大的话，非常费时，最终明显TLE
        """
        # 得到前缀和数组
        pre_sum = self.get_presum(nums)

        # 统计前缀和里面出现的频率
        freq = defaultdict(int)
        res = 0
        for val in pre_sum:
            # target值是我们需要找到的两个前缀和只差
            for target in range(lower, upper + 1):
                # 如果另一个前缀和数出现过，则说明有符合要求的区间
                if val - target in freq:
                    # 加入结果
                    res += freq[val - target]
            # 记录出现频率
            freq[val] += 1

        return res


class Solution2:
    def __init__(self):
        self.count = 0

    def get_presum(self, nums):
        pre_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        return pre_sum

    def merge(self, left, right, lower, upper):
        # 计算有多少个区间和在范围内，核心思路在这
        start = 0
        end = 0
        # 我们遍历左边的所有元素
        # 这里我们只需要对比右数组和左数组的差值区间，因为左右数组内的所有组合已经在之前的递归下计算完了所有符合条件的情况
        for val in left:
            # 如果右边的元素减左边的当前元素小于最小值，说明我们需要继续找左边界，因为左数组是有序的
            while start < len(right) and right[start] - val < lower:
                # 移动左边界指针
                start += 1
            # 同理找右边界，我们需要找到大于最大值的界限
            while end < len(right) and right[end] - val <= upper:
                end += 1
            # 此区间内，所有右数组的数都可以和当前左数组数构成区间和满足条件
            self.count += end - start

        # 合并后的数组
        result = []
        while left and right:
            # 对比两个数组的第一个元素
            # 小的数字弹出并放进去结果数组
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        # 如果左边还有数字，一定是有序的直接加到结果后面
        if left:
            result.extend(left)
        # 同理右边
        if right:
            result.extend(right)

        return result

    def merge_sort(self, nums, lower, upper):
        # 归并排序标准模版
        # 走到底，只有一个元素，直接返回
        if len(nums) < 2:
            return nums
        # 找中间节点
        mid = len(nums) // 2
        # 左右递归，拿到合并成功的数组
        left = self.merge_sort(nums[:mid], lower, upper)
        right = self.merge_sort(nums[mid:], lower, upper)
        # 合并当前节点的左右子树数组
        sub_res = self.merge(left, right, lower, upper)

        return sub_res

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Time O(n + n * log(n))
        Space O(n)
        对一个数组频繁计算一个区间的和，明显要使用前缀和数组。之后就是在一个前缀和数组内找到所有区间组合在给定的范围内。这里参考315，找到
        一个数后面所有比它小的数的思路，我们完全可以使用归并排序的思路，每次左右数组合并的时候，刚好可以判断右数组有多少个数字可以和左数组
        差值在给定的范围内，详细见注释。
        """
        # 得到前缀和数组
        pre_sum = self.get_presum(nums)
        # 归并排序计算个数
        _ = self.merge_sort(pre_sum, lower, upper)

        return self.count


s = Solution2()
print(s.countRangeSum(nums=[-2, 5, -1], lower=-2, upper=2))
print(s.countRangeSum(nums=[0], lower=0, upper=0))
