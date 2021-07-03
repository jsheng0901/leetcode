class Solution:
    def __init__(self):
        self.result = []  # 存放符合条件结果的集合
        self.path = []  # 用来存放符合条件结果

    def backtracking(self, k, target_sum, sum, start_index):
        """
        此题就是组合的模板，每次check总和就行
        targetSum：目标和，也就是题目中的n。
        k：题目中要求k个数的集合。
        sum：已经收集的元素的总和，也就是path里元素的总和。
        startIndex：下一层for循环搜索的起始位置。
        """
        if sum > target_sum:  # 剪枝操作
            return  # 如果path.size() == k 但sum != targetSum 直接返回

        if len(self.path) == k:
            if sum == target_sum:
                self.result.append(self.path)
            # 如果len(path) == k 但sum != target_sum 直接返回
            return

        for i in range(start_index, 10):
            # 此处开始从宽度到深度进行遍历，每一个宽度里面用递归遍历完深度
            sum += i    # 处理
            self.path.append(i)  # 处理节点
            self.backtracking(k, target_sum, sum, i + 1)     # 注意i + 1
            # 调整startIndex
            sum -= i        # 回溯
            self.path = self.path[:len(self.path) - 1]  # 回溯，撤销处理的节点,不要用pop，会改变result的值

    def combinationSum3(self, k: int, n: int) -> [[int]]:

        self.backtracking(k, n, 0, 1)

        return self.result


s = Solution()
print(s.combinationSum3(n=4, k=2))

