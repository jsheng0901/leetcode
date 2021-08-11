class Solution:
    def find_number_of_divisors(self, n):
        if n <= 4:
            return False

        result = [1, n]

        mid = int(n ** 0.5)

        for i in range(2, mid + 1):
            if n % i == 0:
                result.append(i)
                if n // i != i:
                    result.append(n // i)
            if len(result) > 4:
                break

        if len(result) == 4:
            return result
        else:
            return False

    def sumFourDivisors(self, nums: [int]) -> int:
        """
        暴力解法，O(n * sqrt(max(nums))), 每个数字找有多少个factor并且满足题目需求的factors，
        优化过程只能在找factor的时候进行，loop只到sqrt, 长度大于4则停止
        """
        s = 0

        for i in nums:
            if self.find_number_of_divisors(i):
                s += sum(self.find_number_of_divisors(i))

        return s
