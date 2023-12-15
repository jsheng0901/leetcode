class Solution1:
    def dfs(self, node, step):
        if step == 0:
            return 1

        child = self.dfs(node, step - 1)

        return child * node

    def myPow(self, x: float, n: int) -> float:
        """
        Time O(n)
        Space O(1)
        递归写法，后序遍历，每次返回子节点的返回值，然后乘以自己。需要遍历所有n。
        """
        if n >= 0:
            return self.dfs(x, n)
        else:
            return 1 / self.dfs(x, -n)


class Solution2:
    def dfs(self, node, step):
        # 初始情况，如果是0，返回1
        if step == 0:
            return 1
        # 如果走到1，返回自己
        if step == 1:
            return node

        # 如果当前步骤是偶数，我们计算子节点，然后乘以两个子节点结果
        if step % 2 == 0:
            child = self.dfs(node, step // 2)
            return child * child
        # 如果当前步骤是奇数，我们计算子节点，然后乘以子节点结果和当前节点值
        else:
            child = self.dfs(node, step - 1)
            return node * child

    def myPow(self, x: float, n: int) -> float:
        """
        Time O(log(n))
        Space O(1)
        同样是递归写法，后序遍历，这里我们进行二分法拆分，如果n是偶数，比如n=4，可以拆成 n=2 * n=2 的结果，这样有一半我们并不需要计算，
        当n是奇数的时候，比如n=5，可以拆成 n * n=4 的结果，这样我们只需要计算偶数部分再乘以自己即可。大大缩短了运算时间。详细见注释。
        """
        # 当n是正数
        if n >= 0:
            return self.dfs(x, n)
        # 当n是负数
        else:
            return 1 / self.dfs(x, -n)


s = Solution1()
print(s.myPow(x=2.00000, n=10))
print(s.myPow(x=2.00000, n=-2))
print(s.myPow(x=2.10000, n=3))
