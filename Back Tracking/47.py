class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def backtracking(self, nums, used):
        """
        与组合问题不一样的是，排列问题不用在每一层用start index, 因为排列问题，每次都要从头开始搜索，这个地方注意，排列比如从2开始的时候在递归层
        时候我们是从1开始搜索而不是2的下一个元素开始搜索，所以不要每次跳一个index
        例如元素1在[1,2]中已经使用过了，但是在[2,1]中还要再使用一次1

        此题和普通排列的区别是如果给定数组里面有重复数字例如1,1 则不能重复计算，需要去重，方法和组合时候一样，需要提前sort数组然后记录used数组，
        此时used数组不仅是记录同一次递归中是否重复，还是记录同一层loop中是否有相同的数值需要跳过达到去重的目的
        """
        # 此时说明找到了一组
        if len(self.path) == len(nums):
            self.result.append(self.path)
            return

        for i in range(len(nums)):
            # used[i - 1] == true，说明同一树支candidates[i - 1] 使用过
            # used[i - 1] == false，说明同一树层candidates[i - 1] 使用过
            # 而我们要对同一树层使用过的元素进行跳过，同一层去重效率更高，需要走过的node更少
            if i > 0 and nums[i] == nums[i - 1] and used[i - 1] is False:
                continue
            # 同一个递归中我们要判断这个元素是否已经使用过，比如已经使用了1，则不能在下一个使用1，而是2或者3，通过used数组记录使用情况
            if used[i]:
                continue        # path里已经收录的元素，直接跳过
            used[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, used)
            self.path = self.path[: len(self.path) - 1]     # 回溯
            used[i] = False

    def permuteUnique(self, nums: [int]) -> [[int]]:
        used = [False] * len(nums)
        # 首先把给nums排序，让其相同的元素都挨在一起。
        nums.sort()
        self.backtracking(nums, used)

        return self.result


s = Solution()
print(s.permuteUnique(nums=[1, 1, 3]))
