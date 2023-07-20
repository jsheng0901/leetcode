class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def backtracking(self, candidates, target, sum, start_index):
        """
        与求和一样，只是这里树的深度没有限制，直到总和超过target就停止递归，
        此处同样不一定需要传入sum，可以直接sum(self.path)来判断
        如果是一个集合来求组合的话，就需要startIndex，如果是多个集合取组合，各个集合之间相互不影响，那么就不用startIndex
        """
        if sum > target:
            return

        if sum == target:
            self.result.append(self.path)
            return

        for i in range(start_index, len(candidates)):
            # 剪枝，如果总和已经大于target, 则没有必要在进入下一个loop
            if sum + candidates[i] <= target:
                sum += candidates[i]
                self.path.append(candidates[i])
                self.backtracking(candidates, target, sum, i)  # 关键点:不用i+1了，表示可以重复读取当前的数
                sum -= candidates[i]  # 回溯
                self.path = self.path[:len(self.path) - 1]  # 回溯

    def combinationSum(self, candidates: [int], target: int) -> [[int]]:

        self.backtracking(candidates, target, 0, 0)

        return self.result


s = Solution()
print(s.combinationSum(candidates=[2, 3, 5], target=8))
