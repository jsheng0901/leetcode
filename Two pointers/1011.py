from typing import List


class Solution:
    def f(self, weights, x):
        # 定义：当运载能力为 x 时，需要 f(x) 天运完所有货物
        # f(x) 随着 x 的增加单调递减
        days = 0
        i = 0
        while i < len(weights):
            # 尽可能多装货物
            cap = x
            while i < len(weights):
                # 一直往里面装直到超过承载就停止
                if cap < weights[i]:
                    break
                else:
                    cap -= weights[i]
                    i += 1
            # 当前天已经全部装载完成，需要另一天
            days += 1
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Time O(n * log(n))
        Space O(1)
        此题用二分法搜索很巧妙。首先要找到运载能力和运输天数的函数，其次就是在这些运输天数里面找到等于target值的相对应的运载能力。
        总结一下，二分搜索的套路比较固定，如果遇到一个算法问题，能够确定 x, f(x), target 分别是什么，并写出单调函数 f 的代码，
        那么就可以运用二分搜索的思路求解。注意这里的f(x)的输出一定是单调函数换言之就是单调有序的数组里面找target值。
        对于此题船的运载能力就是自变量 x，运输天数和运载能力成反比，所以可以定义 f(x) 表示 x 的运载能力下需要的运输天数，
        target 显然就是运输天数 D，我们要在 f(x) == D 的约束下，算出船的最小载重 x。
        """
        # 左指针起始点，最少要可以装载某一天的weight
        left = max(weights)
        # 右指针表示最少用一天的时间也就是全都装起来
        right = sum(weights)

        # 二分法左边界的模版写法
        while left <= right:
            mid = (left + right) // 2
            # 得到当前承载能力下最少用几天的时间
            if self.f(weights, mid) < days:
                right = mid - 1
            elif self.f(weights, mid) > days:
                left = mid + 1
            elif self.f(weights, mid) == days:
                right = mid - 1

        return left


s = Solution()
print(s.shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))
