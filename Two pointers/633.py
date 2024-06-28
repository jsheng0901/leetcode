import math


class Solution1:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Time O(sqrt(c) * log(c))
        Space O(1)
        利用build-in的平方法写法，直接找是否有满足条件的完全平方数。思路是一样的其实，只是找边界的方式不一样，一个数二分法，一个是build-in
        计算平方根。
        """
        # 搜索区间一定平方根的范围
        for i in range(int(math.sqrt(c)) + 1):
            # 判断完全平方数
            target = c - i * i
            num = int(math.sqrt(target))
            if num * num == target:
                return True

        return False


class Solution2:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Time O(log(c) + sqrt(c))
        Space O(1)
        先二分法找到满足平方根最大的那个数，之后从后向前遍历，找到另一个能组成完全平方数的数，如果有返回true，否则返回false。
        """
        left = 0
        right = c
        # 二分法找第一个满足平方根的最大的数
        while left <= right:
            mid = left + (right - left) // 2

            if mid ** 2 > c:
                right = mid - 1
            # 这里有一个特殊情况，是如果找到直接等于的情况，说明另一个数可以是0，直接返回true
            elif mid ** 2 == c:
                return True
            elif mid ** 2 < c:
                left = mid + 1

        # 遍历找到的区间，从后向前遍历
        for i in range(right, -1, -1):
            target = c - i * i
            # 判断是否是完全平方数
            num = int(math.sqrt(target))
            if num * num == target:
                return True

        # 如果没找到，直接返回false
        return False


class Solution3:
    def binary_search(self, left, right, target):
        while left <= right:
            mid = left + (right - left) // 2

            if mid ** 2 > target:
                right = mid - 1
            elif mid ** 2 == target:
                return True
            elif mid ** 2 < target:
                left = mid + 1

        return False

    def judgeSquareSum(self, c: int) -> bool:
        """
        Time O(sqrt(c) * log(c))
        Space O(1)
        和思路1一模一样，只是换一个方法判断是否是完全平方数
        """
        for i in range(int(math.sqrt(c)) + 1):
            target = c - i * i
            # 用二分法判断是否是完全平方数
            if self.binary_search(0, target, target):
                return True

        return False


s = Solution3()
print(s.judgeSquareSum(c=5))
print(s.judgeSquareSum(c=3))
print(s.judgeSquareSum(c=16))
print(s.judgeSquareSum(c=11))
print(s.judgeSquareSum(c=10000000))
