class Solution1:
    def dp(self, remain, number, graph, mod, memo):
        # 走到最后一步，返回1
        if remain == 0:
            return 1
        # 之前访问过的状态，直接返回结果
        if memo[number][remain] != -1:
            return memo[number][remain]

        # 当前点的子节点返回的path个数
        sub = 0
        for nei in graph[number]:
            # 叠加子节点返回的结果
            sub = (sub + self.dp(remain - 1, nei, graph, mod, memo)) % mod

        # 记录进备忘录
        memo[number][remain] = sub

        return sub

    def knightDialer(self, n: int) -> int:
        """
        Time O(n * k --> n)   since k --> 10
        Space O(n * k --> n)
        DP的思路，每个点都有剩余n的状态，构建备忘录记录状态转移。每个点可以reach的下一个点事固定的，可以提前build好这个graph。
        然后找到走到底的path的个数，base case就是走到底然后返回1，之后就一直叠加，这里起始点可以是每个点，所以要loop一遍所有点作为起始点。
        """
        mod = 10 ** 9 + 7
        # 构建备忘录
        memo = [[-1] * n for _ in range(10)]
        # graph是固定的
        graph = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]

        total = 0
        # 每个点作为起点可以有多少个unique的path
        for number in range(10):
            # 叠加每个点的情况，记得除以MOD
            total = (total + self.dp(n - 1, number, graph, mod, memo)) % mod

        return total


class Solution2:
    def knightDialer(self, n: int) -> int:
        """
        Time O(n)
        Space O(1)
        非常巧妙的思路，这里虽然也是O(n)但是其实快很多，因为不是广义上的推论O(n)。
        详细见link：https://leetcode.com/problems/knight-dialer/editorial/
        """
        if n == 1:
            return 10

        A = 4
        B = 2
        C = 2
        D = 1
        MOD = 10 ** 9 + 7

        for _ in range(n - 1):
            A, B, C, D = (2 * (B + C)) % MOD, A, (A + 2 * D) % MOD, C

        return (A + B + C + D) % MOD


s = Solution2()
print(s.knightDialer(n=1))
print(s.knightDialer(n=2))
