class Solution:
    def dfs(self, total, x, y, target, seen):
        # 找到合理的path了，直接返回
        if total == target:
            return True

        # 不合理的path，不能重复，不能负数或者超出总容量
        if total in seen or total < 0 or total > x + y:
            return False

        # 记录访问过的节点
        seen.add(total)
        # 更新子节点返回值
        sub = False
        # case1，加入水进桶
        sub = sub or self.dfs(total + x, x, y, target, seen)
        sub = sub or self.dfs(total + y, x, y, target, seen)

        # case2，倒出水
        sub = sub or self.dfs(total - x, x, y, target, seen)
        sub = sub or self.dfs(total - y, x, y, target, seen)

        return sub

    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        """
        Time O(x + y)
        Space O(x + y)
        把两个桶的总量当做节点状态，每次我们可以有四个操作，也就是说，我们要遍历一个graph，每个节点四个方向，找到一个path最终节点等于target。
        后续遍历找合理的path标准写法。注意要记录不能走回头路。也就是节点值不能重复。
        """
        # 特殊情况
        if x + y < target:
            return False

        seen = set()
        return self.dfs(0, x, y, target, seen)


class Solution2:
    def gcd(self, a, b):
        """
        找两个数的最大公约数长度的算法
        """
        if b == 0:
            return a

        return b if a % b == 0 else self.gcd(b, a % b)

    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        """
        Time O(n)
        Space O(1)
        数学思路，两个数x, y的最大公约数一定能组成线性组合等式，也就是 ax + by = g，如果g可以被target整除，
        那么也就是说一定有线性组合ax + by = target。
        """
        # 特殊情况
        if x + y < target:
            return False

        # 找到最大公约数
        greatest_common_division = self.gcd(x, y)

        # check是否能被整除
        return target % greatest_common_division == 0


s = Solution2()
print(s.canMeasureWater(x=3, y=5, target=4))
print(s.canMeasureWater(x=2, y=6, target=5))
print(s.canMeasureWater(x=1, y=2, target=3))
print(s.canMeasureWater(x=6, y=7, target=20))
