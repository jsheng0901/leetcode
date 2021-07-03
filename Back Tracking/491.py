class Solution:
    def __init__(self):
        self.result = []
        self.path = []
        self.path_copy = []

    def backtracking(self, nums, start_index):
        """
        与求组合一样，遍历所有叶子节点并记录下来就行，不同点在于去重和check大小
        """
        if len(self.path_copy) > 1:
            self.result.append(self.path_copy)
            # 注意这里不要加return，要取树上的节点

        uset = set()  # 使用set对本层元素进行去重, python查询set比查询数组list要更快

        for i in range(start_index, len(nums)):

            if len(self.path) > 0 and nums[i] < self.path[-1] or nums[i] in uset:
                continue
            uset.add(nums[i])  # 记录这个元素在本层用过了，本层后面不能再用了
            self.path.append(nums[i])  # 子集收集元素
            self.path_copy = self.path.copy()  # deep copy, 否则result里面的数据会随着path的变化而变化
            self.backtracking(nums, i + 1)  # 注意从i + 1 开始，元素不重复取
            # self.path = self.path[: len(self.path) - 1]     # 回溯
            self.path.pop()  # 回溯 此处不需要覆盖，因为我们已经引入了一个copy

    def findSubsequences(self, nums: [int]) -> [[int]]:
        # 此题不能先sort在去重，因为原始list里面的顺序有意义，不能sort
        self.backtracking(nums, 0)

        return self.result


s = Solution()
print(s.findSubsequences(nums=[4, 6, 7, 7]))
