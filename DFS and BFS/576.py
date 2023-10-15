class Solution1:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(self, m, n, i, j, move, memo):
        # base case，找到一条出界路径
        if i < 0 or i >= m or j < 0 or j >= n:
            return 1

        # 无法在有限的步数内出界
        if move == 0:
            return 0

        # 避免冗余计算
        if memo[i][j][move] != -1:
            return memo[i][j][move]

        # 后序遍历的逻辑，统计当前节点所有子节点的返回结果并在当前节点处理
        # 状态转移关系：
        # 在 move 之内从 (i, j) 踢出界的路径数量等于 在 move - 1 之内从 (i, j) 的相邻位置踢出界的路径数量之和
        res = 0
        # 遍历四个临近方向
        for direction in self.directions:
            # 下一个节点方向
            next_i = i + direction[0]
            next_j = j + direction[1]
            # 处理返回结果，统计路径和
            res += self.dfs(m, n, next_i, next_j, move - 1, memo)

        # 存储当前节点的结果进备忘录
        memo[i][j][move] = res % 1000000007

        return res

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        Time O(n * m * move)    遍历完整个备忘录
        Space O(n * m * move)
        核心思想，到达当前点 [i, j] 的路径总数等于 到达这个点临近的四个点的路径总数和。把graph当做树，边界当做树结构中的空节点，
        当我们走到空节点的时候就找到了一条根节点到空节点的path，此时返回 1，类似后续遍历思路，上一个节点的走过path总和则等于子节点的四个方向
        的返回总和，同理一路递归到其实点及树里面的根节点。因为我们这里可以重复访问节点，并且graph是全连接起来的树，
        所以有很多重复走过的节点，用一个备忘录记录走过的同样的位置的结果。
        """
        # 构建备忘录，这里 move 要 +1，因为 move 起始为 1，备忘录初始化为特殊值 -1
        memo = [[[-1] * (maxMove + 1) for _ in range(n)] for _ in range(m)]

        # 按照定义，计算从 (startRow, startColumn) 开始，最大移动次数为 maxMove 的出界路径数量
        return self.dfs(m, n, startRow, startColumn, maxMove, memo)


class Solution2:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.path = 0

    def dfs(self, m, n, i, j, move):

        # 遍历四个临近方向
        for direction in self.directions:
            # 下一个节点方向
            next_i = i + direction[0]
            next_j = j + direction[1]
            # 有限的步数则跳入下一个节点
            if move > 0:
                # 遇到根节点及越界，找到一条path
                if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                    # 全局记录 +1
                    self.path += 1
                else:
                    # 没有越界，继续递归
                    self.dfs(m, n, next_i, next_j, move - 1)

        return

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        Time O(4 ^ move)    四个方向，每个一步有四个选择
        Space O(move)       递归深度
        暴力解法，把graph当做树，边界当做树结构中的空节点，当我们走到空节点的时候就找到了一条根节点到空节点的path，此时全局计数器 +1。
        类似前序遍历思路，这里用 DFS 写法，在loop里面处理下一个子节点，不在loop外处理当前节点。
        注意此方法一定会超时，因为方法一里面已经说明了，我们有很多重复的走过的节点情况。必须使用备忘录来记录。
        另一个重点：使用备忘录时我们不能用全局变量来记录path，必须使用后续遍历递归的思路处理返回值，再记录进备忘录，具体操作参考方案1。
        因为如果用全局记录，则遍历到某个节点并记录进备忘录的时候，我们记录的不是走到这个节点可以有多少走到根节点的path方式，
        我们记录的是走到此节点时候，目前整个图总共有多少条走到根节点的path方式。此时备忘录的定义则完全弄错。
        换句话来说，带备忘录的 DFS 可以理解为就是 DP，备忘录就 DP 数组，我们需要记录的当前节点返回结果进备忘录，
        所以带备忘录的 DFS/BFS 不能采用全局变量记录。
        具体备忘录怎么设置维度和定义参考递归中会变动的参数，因为设置备忘录的意义就是避免重复进递归函数。
        """
        # 按照定义，计算从 (startRow, startColumn) 开始，最大移动次数为 maxMove 的出界路径数量
        self.dfs(m, n, startRow, startColumn, maxMove)

        return self.path


s = Solution1()
print(s.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1))
print(s.findPaths(m=8, n=7, maxMove=16, startRow=1, startColumn=5))
