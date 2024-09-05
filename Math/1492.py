class Solution1:
    def kthFactor(self, n: int, k: int) -> int:
        """
        Time O(n)
        Space O(1)
        最直接的暴力思路，从1开始注意遍历查看是不是因子，如果是就叠加记录个数，遇到第k个的话就直接返回结果。如果没有遇到k，返回-1
        """
        count = 0
        for i in range(1, n + 1):
            # 如果是因子，累加
            if n % i == 0:
                count += 1

            # 找到第k因子，直接返回
            if count == k:
                return i

        # 没找到直接返回-1
        return -1


class Solution2:
    def kthFactor(self, n: int, k: int) -> int:
        """
        Time O(n // 2)
        Space O(1)
        其实我们并不需要遍历n的后半部分，因为一定不是因子，出去n本身，我们只需要遍历前半部分即可，其它思路一样。
        """
        count = 0
        # 遍历前半部分
        for i in range(1, (n // 2) + 1):
            if n % i == 0:
                count += 1

            if count == k:
                return i

        # 如果加上自己还不是第k个的话，那说明找不到第k个，直接返回-1
        return n if count + 1 == k else -1


class Solution3:
    def kthFactor(self, n: int, k: int) -> int:
        """
        Time O(sqrt(n))
        Space O(1)
        其实找因子，完全可以只找到sqrt(n)的部分即可，如果 n 有一个因子 x，那么它必然有一个另一个因子 n/x，
        这两个因子中至少有一个是小于等于sqrt(n)，先找到[1, sqrt(n)]的区间内有多少因子，如果找到了第k个，就直接返回，
        如果找不到说明第k个因子在[sqrt(n), n]区间内，此时我们只需要反向遍历[1, sqrt(n)]区间找 n / x 这个因子即可。
        特殊情况如果 n 是完全平方数，那么满足 x^2 = n 的因子 x 被枚举了两次，需要忽略其中的一次。
        """
        count = 0
        # 因子初始值
        factor = 1
        # 遍历 [1, sqrt(n)] 区间
        while factor * factor <= n:
            if n % factor == 0:
                count += 1
                # 如果找到了第k个，直接返回
                if count == k:
                    return factor
            # 因子继续扩大
            factor += 1
        # 跳出循环的时候是平方大于n的时候，需要 -1
        factor -= 1
        # 特殊情况
        if factor * factor == n:
            factor -= 1

        # 反向遍历 [1, sqrt(n)] 区间，得到 n / x 另一个因子
        while factor > 0:
            if n % factor == 0:
                count += 1
                # 找了第k个
                if count == k:
                    # 应该是 n / x 这个因子
                    return n // factor
            factor -= 1
        # 找不到
        return -1


s = Solution2()
print(s.kthFactor(n=12, k=3))
print(s.kthFactor(n=7, k=2))
print(s.kthFactor(n=4, k=4))
