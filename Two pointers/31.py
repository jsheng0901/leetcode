class Solution:
    # def __init__(self):
    #     self.res = []
    #     self.string = ''
    #
    # def backtracking(self, nums, used):
    #     if len(self.string) == len(nums):
    #         self.res.append(int(self.string))
    #         return
    #
    #     for i in range(len(nums)):
    #         if used[i] == 1:
    #             continue
    #         else:
    #             self.string += str(nums[i])
    #             used[i] = 1
    #         self.backtracking(nums, used)
    #         self.string = self.string[:-1]
    #         used[i] = 0
    #
    #     return

    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        此题逻辑：找到第一个下降点，再找到第一个大于下降点的数的index，swap这两个数，然后把下降点后所有数字收尾swap
        因为从后向前遍历当遇到不是递增的第一个下降点的时候就是要交换位置的数字
        """
        # used = [0] * len(nums)
        # self.backtracking(nums, used)
        #
        # self.res.sort()
        # target = int("".join([str(n) for n in nums]))
        # for i in range(len(self.res)):
        #     if self.res[i] == target and i != len(self.res) - 1:
        #         return [int(x) for x in str(self.res[i + 1])]
        #     elif self.res[i] == target:
        #         return [int(x) for x in str(self.res[0])]
        down_index = None
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                down_index = i
                break
        # 如果没有下降点，重新排列
        if down_index is None:
            nums.reverse()
        else:
            # 第二步，从后往前，找到比下降点大的数，对换位置
            for i in range(len(nums) - 1, -1, -1):
                if nums[down_index] < nums[i]:
                    nums[down_index], nums[i] = nums[i], nums[down_index]
                    break
            # 第三部，重新排列下降点之后的数
            i, j = down_index + 1, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1


s = Solution()
print(s.nextPermutation(nums=[1, 2, 3]))
