class Solution:
    def __init__(self):
        self.result = []
        self.path = []
        self.path_copy = []

    def backtracking(self, nums, start_index, used):
        """
        与求组合一样，只是这里不要求剪值也不要求限制节点，遍历所有叶子节点并记录下来就行
        """
        self.result.append(self.path_copy)   # 收集子集，要放在终止添加的上面，否则会漏掉自己

        if start_index >= len(nums):
            return

        for i in range(start_index, len(nums)):
            # used[i - 1] == true，说明同一树支candidates[i - 1] 使用过
            # used[i - 1] == false，说明同一树层candidates[i - 1] 使用过
            # 而我们要对同一树层使用过的元素进行跳过
            if i > 0 and nums[i] == nums[i - 1] and used[i - 1] is False:
                continue
            self.path.append(nums[i])   # 子集收集元素
            self.path_copy = self.path.copy()           # deep copy, 否则result里面的数据会随着path的变化而变化
            used[i] = True
            self.backtracking(nums, i + 1, used)      # 注意从i + 1 开始，元素不重复取
            used[i] = False
            # self.path = self.path[: len(self.path) - 1]     # 回溯
            self.path.pop()                                   # 回溯 此处不需要覆盖，因为我们已经引入了一个copy

    def subsetsWithDup1(self, nums: [int]) -> [[int]]:
        used = [False] * len(nums)
        # 首先把给nums排序，让其相同的元素都挨在一起。
        nums.sort()
        self.backtracking(nums, 0, used)

        return self.result

    def subsetsWithDup2(self, nums: [int]) -> [[int]]:
        """另一种不需要全局变量的方法，全局变量容易引发之前的指代数据变化"""
        result = []
        path = []

        def backtracking(nums, used, start_index):
            result.append(path[:])

            if start_index >= len(nums):
                return

            for i in range(start_index, len(nums)):
                if i > 0 and used[i - 1] is False and nums[i - 1] == nums[i]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtracking(nums, used, i + 1)
                path.pop()
                used[i] = False

            return

        used = [False] * len(nums)
        nums.sort()
        backtracking(nums, used, 0)

        return result


s = Solution()
print(s.subsetsWithDup1(nums=[1, 2, 2]))
