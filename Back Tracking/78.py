class Solution:
    def __init__(self):
        self.result = []
        self.path = []
        self.path_copy = []

    def backtracking(self, nums, start_index):
        """
        与求组合一样，只是这里不要求剪值也不要求限制节点，遍历所有叶子节点并记录下来就行
        """
        self.result.append(self.path_copy)   # 收集子集，要放在终止添加的上面，否则会漏掉自己

        if start_index >= len(nums):
            return

        for i in range(start_index, len(nums)):
            self.path.append(nums[i])   # 子集收集元素
            self.path_copy = self.path.copy()           # deep copy, 否则result里面的数据会随着path的变化而变化
            self.backtracking(nums, i + 1)      # 注意从i + 1 开始，元素不重复取
            self.path = self.path[: len(self.path) - 1]     # 回溯

    def subsets(self, nums: [int]) -> [[int]]:
        self.backtracking(nums, 0)

        return self.result

    def subsets1(self, nums: [int]) -> [[int]]:
        """另一种写法，不要class的全局变量，这样不会改动之前的数据当path改动的时候，只需要local变量"""
        res = []
        path = []

        def backtrack(nums, startIndex):
            res.append(path[:])  # 收集子集，要放在终止添加的上面，否则会漏掉自己
            for i in range(startIndex, len(nums)):  # 当startIndex已经大于数组的长度了，就终止了，for循环本来也结束了，所以不需要终止条件
                path.append(nums[i])
                backtrack(nums, i + 1)  # 递归
                path.pop()  # 回溯

s = Solution()
print(s.subsets(nums=[2, 3, 5]))
