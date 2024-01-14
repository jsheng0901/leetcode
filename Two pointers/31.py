from typing import List


class Solution1:
    def __init__(self):
        self.res = []
        self.string = ''

    def backtracking(self, nums, used):
        if len(self.string) == len(nums):
            self.res.append(int(self.string))
            return

        for i in range(len(nums)):
            # 同一条path不能重复使用同样的数字，比如不能[1, 2, 3]不能重复使用变成[1, 1, 2]
            if used[i] == 1:
                continue
            else:
                self.string += str(nums[i])
                used[i] = 1
            self.backtracking(nums, used)
            self.string = self.string[:-1]
            # 同一层可以重复使用，比如之前使用了 1，下一个loop可以使用 2，并且在 2这个path下可以使用 1，所有这里要回溯
            used[i] = 0

        return

    def nextPermutation(self, nums: [int]) -> List[int]:
        """
        Time O(n! + nlog(n) + n)
        Space O(n)
        先回溯找到所有排列的结果，然后对结果进行排序，之后找到target结果的下一个结果并返回。
        此方法很明显超时，拿到所有排列结果的回溯很费时。
        """
        # 回溯拿所有排列结果
        used = [0] * len(nums)
        self.backtracking(nums, used)

        # sort 排列结果
        self.res.sort()
        # list 转 int
        target = int("".join([str(n) for n in nums]))
        # 找到target数字的下一个数字
        for i in range(len(self.res)):
            if self.res[i] == target and i != len(self.res) - 1:
                return [int(x) for x in str(self.res[i + 1])]
            elif self.res[i] == target:
                return [int(x) for x in str(self.res[0])]


class Solution2:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Time O(n)
        Space O(1)
        Do not return anything, modify nums in-place instead.
        此题逻辑：
        1. 找到第一个下降点，下降低的意义是从后往前第一个index + 1大于 index的点。
        2. 再从后往前在index的右边找到第一个大于下降点的数的index，swap这两个数。
        3. 然后把下降点后所有数字收尾swap，因为从后向前遍历当遇到不是递增的第一个下降点的时候此时后面这一部分序列已经是递减的顺序了，
           所以最后直接reverse就是递增的序列
        """
        down_index = None
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                down_index = i
                break
        # 如果没有下降点，说明此时数组已经是最大的排列情况了，重新reverse即可
        if down_index is None:
            nums.reverse()
        else:
            # 第二步，从后往前，找到第一个比下降点大的数，也就是大于下降点的最小的数，对换位置
            for i in range(len(nums) - 1, -1, -1):
                if nums[down_index] < nums[i]:
                    nums[down_index], nums[i] = nums[i], nums[down_index]
                    break
            # 第三步，重新排列下降点之后的数
            i, j = down_index + 1, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1


s = Solution1()
print(s.nextPermutation(nums=[1, 2, 3]))
