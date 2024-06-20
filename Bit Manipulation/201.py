class Solution1:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Time O(n)
        Space O(1)
        很简单的思路，每个进行位运算的叠加，但是明显如果range太大会超时TLE。
        """
        res = left
        # 位运算叠加
        for i in range(left + 1, right + 1):
            res &= i

        return res


class Solution2:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Time O(1)
        Space O(1)
        因为位运算的叠加特殊性，必须要满足每个位置都是1才会最终是1，否则是0，也就是说，我们其实需要做的是找到起点和终点数字
        的common prefix为1位置。这里可以用shift来找，一直往右shift，直到左右数字相等。同时记录shift多少此，最终结果在shift左边回去。
        """
        # 记录shift了多少此
        shift = 0
        # 找到common prefix为1的位置
        while left < right:
            # 右shift一位
            left = left >> 1
            right = right >> 1
            # 记录次数
            shift += 1
        # shift左边回去
        return left << shift


class Solution3:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Time O(1)
        Space O(1)
        思路是一样的，还是同样地消除最右边的1，这里利用一个特殊公式，相邻两个数的位运算加法得到的数刚好会消除最右边的1。
        """
        # 从左向右做位运算叠加
        while left < right:
            # 消除最右边的1，一直更新右指针
            right = right & (right - 1)

        # 最终消除到和左指针一样的时候就是我们要的结果
        return right


s = Solution3()
print(s.rangeBitwiseAnd(left=5, right=7))
print(s.rangeBitwiseAnd(left=1, right=2147483647))
