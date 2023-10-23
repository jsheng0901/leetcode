from typing import List


class Solution1:
    def __init__(self):
        self.result = float('-inf')
        self.path = []

    def backtracking(self, nums, num_ballons):
        # 遇到终点，及结束一条path的搜索，注意这里不能直接用index判断，因为nums输入一直在变。气球戳破后等同于移除此元素从nums中。
        if len(self.path) == num_ballons:
            # 统计当前排列的结果
            cur_sum = sum(self.path)
            # 更新最大值
            self.result = max(self.result, cur_sum)
            return

        for i in range(len(nums)):
            # 统计当前层，当前节点气球戳破得到的硬币
            value = 0
            # 四种情况对应如何得到硬币
            if len(nums) - 1 > i > 0:
                value = nums[i - 1] * nums[i] * nums[i + 1]
            elif len(nums) == 1:
                value = nums[i]
            elif i == 0:
                value = nums[i] * nums[i + 1]
            elif i == len(nums) - 1:
                value = nums[i - 1] * nums[i]
            # 加入path记录当前节点得到的最终值
            self.path.append(value)
            # 继续递归下一个排列选择，这里要移除已经戳破的气球，不然会影响后续计算硬币的值，这里是和真正排列不一样的地方。
            self.backtracking(nums[:i] + nums[i + 1:], num_ballons)
            # 回溯，撤销当前选择
            self.path.pop()

        return

    def maxCoins(self, nums: List[int]) -> float:
        """
        Time O(n!)
        Space O(n!)
        回溯的思维模式，每次戳破的气球相当于就是排列的顺序，回溯遍历所有排列的结果，每次记录戳破气球得到的硬币，
        走完一次排列，记录一下当前最大值，继续回溯走完所有排列。
        回溯的思想这里类似前序遍历，因为我们是在每次处理当前节点的时候计算得到硬币的值。然后通过全局变量记录到走到底及叶子结点。
        回溯会超时，因为有大量的重复计算，ex：[3, 1, 5, 8]，当我们排列完[3, 1]的时候要在排列一次[5, 8]，
        然而当我们排列完[1, 3]的时候需要再次计算一遍[5, 8]。会超时对于第二和三个测试数据。
        """
        # 记录总共有多少个气球
        num_ballons = len(nums)
        # 开始递归
        self.backtracking(nums, num_ballons)

        # 返回最大值
        return self.result


class Solution2:
    def dp(self, nums, memo):
        # 如果已经计算过，这里nums序列化为字典的key来存储结果，直接返回最大值
        if str(nums) in memo:
            return memo[str(nums)]

        # 走到底了只有一个元素，此时最大硬币值就是自己，返回结果并记录进备忘录
        if len(nums) == 1:
            memo[str(nums)] = nums[0]
            return nums[0]

        # 同一层最大值，先初始化为负无穷
        res = float('-inf')
        for i in range(len(nums)):
            # 当前选择的气球得到的硬币值
            value = 0
            # 三种情况可能得到的值
            if len(nums) - 1 > i > 0:
                value = nums[i - 1] * nums[i] * nums[i + 1]
            elif i == 0:
                value = nums[i] * nums[i + 1]
            elif i == len(nums) - 1:
                value = nums[i - 1] * nums[i]
            # 递归进入，戳破气球后下一个子结果，并返回硬币值
            sub_res = self.dp(nums[:i] + nums[i + 1:], memo)
            # 当前节点对应的输入nums得到的最大硬币结果为，当前戳破的气球得到的值加上子结果返回的最大值
            res = max(res, value + sub_res)

        # 记录进备忘录
        memo[str(nums)] = res
        # 返回最大值
        return res

    def maxCoins(self, nums: List[int]) -> float:
        """
        Time O(n!)
        Space O(n!)
        动态规划思想，我们把整体问题拆分成子问题，我们用后续遍历的思想，加上贪心的思想，要想全局最大，则从最小结构开始及一个元素到所有元素。
        我们每次都选择最大的得到硬币的方式。返回最大值，然后自底向上返回结果。同时带一个备忘录，记录当前输入nums对应的得到最大硬币值的结果。
        测试还是会超时，测试三通过不了。
        """
        # 初始化备忘录，记录每次变化的参数数组nums对应得到的最大硬币结果。
        memo = {}
        # 开始递归
        return self.dp(nums, memo)


class Solution3:
    def maxCoins(self, nums: List[int]) -> float:
        """
        Time O(n^2)
        Space O(n^2)
        需要多次解读。
        """
        n = len(nums)
        # 添加两侧的虚拟气球
        points = [0] * (n + 2)
        points[0], points[n + 1] = 1, 1
        for i in range(1, n + 1):
            points[i] = nums[i - 1]
        # base case 已经都被初始化为 0
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        # 开始状态转移
        # i 应该从下往上
        for i in range(n, -1, -1):
            # j 应该从左往右
            for j in range(i + 1, n + 2):
                # 最后戳破的气球是哪个？
                for k in range(i + 1, j):
                    # 择优做选择
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + points[i] * points[j] * points[k]
                    )
        return dp[0][n + 1]


s = Solution3()
print(s.maxCoins(nums=[3, 1, 5, 8]))
print(s.maxCoins(nums=[7, 9, 8, 0, 7, 1, 3, 5, 5, 2, 3]))
print(s.maxCoins(nums=[8, 3, 4, 3, 5, 0, 5, 6, 6, 2, 8, 5, 6, 2, 3, 8, 3, 5, 1, 0, 2]))
