from typing import List


class Solution1:
    def __init__(self):
        self.res = []

    def merge(self, left, right):
        # 先找出来当前左边数字有多少个右边数字比它小
        p1 = len(left) - 1
        p2 = len(right) - 1
        # 用从后向前的遍历思路，因为如果当前数字比右边的有序数组最大的还大的话，我们就不需要继续遍历右边剩下的部分
        while p1 >= 0 and p2 >= 0:
            left_num, left_index = left[p1][0], left[p1][1]
            right_num, right_index = right[p2][0], right[p2][1]
            # 左边大于右边的时候
            if left_num > right_num:
                # 右边前面所有的数都符合要求，因为是有序的数组
                self.res[left_index] += p2 + 1
                p1 -= 1
            # 左边小于右边的时候，移动左边继续找，不再需要移动右边因为右边也是有序递增的数组
            else:
                p2 -= 1

        # 再进行合并数组
        result = []
        while left and right:
            # 对比两个数组的第一个元素
            # 小的数字弹出并放进去结果数组
            if left[0][0] <= right[0][0]:
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
        if len(nums) <= 1:
            return nums
        # 找中间节点
        mid = len(nums) // 2
        # 左右递归，拿到合并成功的数组
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        # 合并当前节点的左右子树数组
        sub = self.merge(left, right)

        return sub

    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        Time O(n * log(n))
        Space O(n)
        归并排序的思路，在进行merge的时候先算出多少个右边的数比当前左边的数少。这里思路同493。合并的时候其实需要遍历两次数组，其实会变慢。
        """
        # 先把index拿出来组合在一起，这样方便后续找到result数组位置
        nums_with_index = []
        for i, v in enumerate(nums):
            nums_with_index.append((v, i))

        self.res = [0] * len(nums)
        result = self.merge_sort(nums_with_index)

        return self.res


class Solution2:
    def __init__(self):
        self.res = []

    def merge(self, left, right):

        p1 = 0
        p2 = 0
        # 存储合并后结果的数组
        result = []
        while p1 < len(left) and p2 < len(right):
            left_num, left_index = left[p1][0], left[p1][1]
            right_num, right_index = right[p2][0], right[p2][1]
            # 左边小于等于右边的时候，此时说明右边前面的所有数都小于左边当前数，因为是递增数组
            if left_num <= right_num:
                # 加入合并的结果
                result.append(left[p1])
                # 右边前面所有的数都符合要求，因为是有序的数组
                self.res[left_index] += p2
                # 移动左指针
                p1 += 1
            # 左边大于右边的时候，移动右边继续找，不再需要移动左边因为左边也是有序递增的数组
            else:
                # 加入合并的结果
                result.append(right[p2])
                # 移动右指针
                p2 += 1

        # 左边还有没走完的数，此时后面所有数都比当前所有右边数组每个数都大
        while p1 < len(left):
            result.append(left[p1])
            # 同理更新结果
            self.res[left[p1][1]] += len(right)
            p1 += 1
        # 同理右边
        while p2 < len(right):
            result.append(right[p2])
            p2 += 1

        # 返回合并后的结果
        return result

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        sub = self.merge(left, right)

        return sub

    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        Time O(n * log(n))
        Space O(n)
        归并排序的思路，同思路1，但是其实我们并不需要单调分开计算个数和合并数组。可以合在一起计算。这样更快对比思路1，详细见注释。
        """
        nums_with_index = []
        for i, v in enumerate(nums):
            nums_with_index.append((v, i))

        self.res = [0] * len(nums)
        result = self.merge_sort(nums_with_index)

        return self.res


s1 = Solution2()
print(s1.countSmaller(nums=[5, 2, 6, 1]))
s2 = Solution2()
print(s2.countSmaller(nums=[1, 9, 7, 8, 5]))
