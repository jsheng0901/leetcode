# Union Find 模板题，一下是Union Find 模板。
from typing import List


class UnionFind:
    def __init__(self, n: int):
        """
        Time O(n)
        Space O(n)
        """
        self.parent = list(range(n))
        self.count = n
        # 可以引入size数组来达到树的生长相对平衡，达到log(n)级别的树的高度，这样find，union and connected速度大大提升到log(n)
        # self.size = [1] * n

    def find(self, x: int) -> int:
        """
        Time O(1)
        Space O(1)
        引入路径压缩技巧后的时间复杂度
        """
        # 不过这里引入路径压缩技巧，那么 size 数组的平衡优化就不是特别必要了
        if self.parent[x] != x:
            # 此技巧不好理解，大致上是，先找到根节点，然后把 x 到根节点之间的所有节点直接接到根节点下面
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        """
        Time O(1)
        Space O(1)
        引入路径压缩技巧后的时间复杂度
        """

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        # 引入平衡数组记录重量后，小树接到大树下面，较平衡
        # if self.size[root_x] > self.size[root_y]:
        #     self.parent[root_y] = root_x
        #     self.size[root_x] += self.size[root_y]
        # else:
        #     self.parent[root_x] = root_y
        #     self.size[root_y] += self.size[root_x]
        self.parent[root_x] = root_y
        self.count -= 1

    def connected(self, x: int, y: int) -> bool:
        """
        Time O(1)
        Space O(1)
        引入路径压缩技巧后的时间复杂度
        """

        root_x = self.find(x)
        root_y = self.find(y)

        return root_x == root_y

    def count(self) -> int:
        """
        Time O(1)
        Space O(1)
        """

        return self.count


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """
        Time O(n)   n is number of equations
        Space O(n)
        构造union find class，把所有等于的情况的字母连接起来，对于不等于的我们判断是否被连起来过，如果被连起来过则说明此等式组合不能成立
        """
        # 26 个英文字母初始化
        union_find = UnionFind(26)

        # 先让相等的字母形成连通分量
        for equation in equations:
            if equation[1] == "=":
                x = equation[0]
                y = equation[3]
                # 有个技巧，把字母转化成数字顺序这里
                union_find.union(ord(x) - ord('a'), ord(y) - ord('a'))

        # 检查不等关系是否打破相等关系的连通性
        for equation in equations:
            if equation[1] == "!":
                x = equation[0]
                y = equation[3]
                # 如果相等关系成立，就是逻辑冲突
                if union_find.connected(ord(x) - ord('a'), ord(y) - ord('a')):
                    return False

        return True
