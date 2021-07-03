class Solution:
    def __init__(self):
        self.result = []    # 存放组合集合
        self.path = []      # 符合条件的组合

    def backtracking(self, candidates, target, sum, start_index, used):
        """
        与求和一样，但是我们不能在同一层树里面使用同样的数字，同一个树枝里面可以重复
        """
        if sum > target:
            return

        if sum == target:
            self.result.append(self.path)
            return

        for i in range(start_index, len(candidates)):
            # 剪枝，如果总和已经大于target, 则没有必要在进入下一个loop
            if sum + candidates[i] <= target:
                # used[i - 1] == true，说明同一树支candidates[i - 1] 使用过, 因为同一层使用过会把false转化为true，并且没有回溯
                # used[i - 1] == false，说明同一树层candidates[i - 1] 使用过, 同一层此时已近回溯过，所以当false的时候为之前用过
                # 要对同一树层使用过的元素进行跳过
                if i > 0 and candidates[i] == candidates[i - 1] and used[i - 1] is False:
                    continue
                sum += candidates[i]
                self.path.append(candidates[i])
                used[i] = True
                self.backtracking(candidates, target, sum, i + 1, used)  # 关键点: 这里是i+1，每个数字在每个组合中只能使用一次
                used[i] = False
                sum -= candidates[i]  # 回溯
                self.path = self.path[:len(self.path) - 1]  # 回溯

    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        used = [False] * len(candidates)
        # 首先把给candidates排序，让其相同的元素都挨在一起。
        candidates.sort()
        self.backtracking(candidates, target, 0, 0, used)

        return self.result


s = Solution()
print(s.combinationSum2(candidates=[1, 1, 2], target=2))
