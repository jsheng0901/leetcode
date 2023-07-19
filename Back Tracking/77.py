# def backtracking(parameter):
#     if 终止条件:
#         存放结果
#         return
#
#     for 选择：本层集合中元素（树中节点孩子的数量就是集合的大小）:
#         处理节点
#         backtracking(路径，选择列表)  # 递归
#         回溯，撤销处理结果
#
# 回溯的模板

class Solution:
    def __init__(self):
        self.result = []  # 存放符合条件结果的集合
        self.path = []  # 用来存放符合条件结果

    def backtracking(self, n, k, start_index):
        """
        Time O(n * k^n) k是回溯中递归的次数
        Space O(n)
        """
        if len(self.path) == k:
            self.result.append(self.path)
            return

        for i in range(start_index,  n - (k - len(self.path)) + 2):
            # 此处开始从宽度到深度进行遍历，每一个宽度里面用递归遍历完深度， 此处含有减枝的过程
            # 减枝的过程就是在loop的时候限制loop的range，ex: 4 - (4 - 0) + 2 == 2 --> range(1, 2)只能取到一个数1
            self.path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1)  # 递归
            self.path = self.path[:len(self.path)-1]  # 回溯，撤销处理的节点,不要用pop，会改变result的值

    def combine(self, n: int, k: int) -> [[int]]:

        self.backtracking(n, k, 1)

        return self.result


s = Solution()
print(s.combine(n=4, k=2))
