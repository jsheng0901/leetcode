class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def backtracking(self, nums, used):
        """
        与组合问题不一样的是，排列问题不用在每一层用start index, 因为排列问题，每次都要从头开始搜索，这个地方注意，排列比如从2开始的时候在递归层
        时候我们是从1开始搜索而不是2的下一个元素开始搜索，所以不要每次跳一个index
        例如元素1在[1,2]中已经使用过了，但是在[2,1]中还要再使用一次1
        """
        # 此时说明找到了一组
        if len(self.path) == len(nums):
            self.result.append(self.path)
            return

        for i in range(len(nums)):
            # 同一个递归中我们要拍段这个元素是否已经使用过，比如已经使用了1，则不能在下一个使用1，而是2或者3，通过used数组记录使用情况
            if used[i]:
                continue        # path里已经收录的元素，直接跳过
            used[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, used)
            self.path = self.path[: len(self.path) - 1]     # 回溯
            used[i] = False

    def permute(self, nums: [int]) -> [[int]]:
        used = [False] * len(nums)
        self.backtracking(nums, used)

        return self.result


s = Solution()
print(s.permute(nums=[1, 2, 3]))
