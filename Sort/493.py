from typing import List


class Solution1:
    def __init__(self):
        self.pairs = 0

    def count(self, left, right):
        # 计算所有符合条件的pairs，遍历所有组合
        for i in left:
            for j in right:
                if i > 2 * j:
                    self.pairs += 1

        return

    def merge_sort(self, nums):
        if len(nums) < 2:
            return
        # 找中间节点
        middle = len(nums) // 2
        # 左右递归
        left = nums[: middle]
        right = nums[middle:]
        self.merge_sort(left)
        self.merge_sort(right)
        # 计算当前左右数组
        self.count(left, right)

        return

    def reversePairs(self, nums: List[int]) -> int:
        """
        Time O(n^2)
        Space O(n)
        利用归并排序的思路，进行分治计算，每一次对比左右数组的时候需要遍历每个元素，所以其实还是O(n^2)的操作。并没有利用到排序完后的优势。
        明显TLE。
        """
        self.merge_sort(nums)

        return self.pairs


class Solution2:
    def __init__(self):
        self.pairs = 0

    def merge_count(self, left, right):
        # 计算有多少个合理的pairs
        p1 = 0
        p2 = 0
        while p1 < len(left) and p2 < len(right):
            # 左边大于右边的时候
            if left[p1] > 2 * right[p2]:
                # 左边后面所有的数都符合要求，因为是有序的数组
                self.pairs += len(left) - p1
                p2 += 1
            # 左边小于右边的时候，移动左边继续找，不再需要移动右边因为右边也是有序递增的数组
            else:
                p1 += 1

        # 再进行合并数组
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

        # 返回合并后的结果
        return result

    def merge_sort(self, nums):
        if len(nums) < 2:
            return nums
        # 找中间节点
        middle = len(nums) // 2
        # 左右递归，拿到合并成功的数组
        left = self.merge_sort(nums[: middle])
        right = self.merge_sort(nums[middle:])
        # 合并当前节点的左右子树数组
        sub = self.merge_count(left, right)

        return sub

    def reversePairs(self, nums: List[int]) -> int:
        """
        Time O(n * log(n))
        Space O(n)
        这次我们利用归并排序的优势，每次对比的是两个有序数组，这样只有左边数组的出现满足条件的pairs时候，左边数组后面所有的数都可以和当前右边
        数组数构成合理的pairs。不需要遍历两个数组所有数。
        """
        sorted_nums = self.merge_sort(nums)

        return self.pairs


s1 = Solution2()
print(s1.reversePairs(nums=[1, 3, 2, 3, 1]))
s2 = Solution2()
print(s2.reversePairs(nums=[2, 4, 3, 5, 1]))
