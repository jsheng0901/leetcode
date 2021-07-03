class Solution:
    def maxSatisfied(self, customers: [int], grumpy: [int], minutes: int) -> int:
        """
        O(len(customers)) time
        此题一定要减少计算sum的过程，尽量用叠加，而不是每次计算sum重头来一次
        滑动窗口移动size为minute的窗口，然后同时计算窗口左边和右边的sum判断总和大小并更新result，
        一定不要找到最大窗口后再计算两边的总和，这样会超时，因为sum的重新计算也是O(n)的time
        :param customers:
        :param grumpy:
        :param minutes:
        :return:
        """
        left = 0
        right = minutes
        mid_sum = 0
        left_sum = 0
        right_sum = 0
        result = 0
        for j in range(minutes, len(customers)):
            if grumpy[j] == 0:
                right_sum += customers[j]
        for i in range(minutes, len(customers)+1):
            left = i - minutes
            right = i
            mid_sum = sum(customers[i - minutes: i])
            if left > 0 and grumpy[left - 1] == 0:
                left_sum += customers[left-1]
            if minutes < right <= len(customers) and grumpy[right-1] == 0:
                right_sum -= customers[right-1]

            tmp_sum = mid_sum + left_sum + right_sum

            if tmp_sum > result:
                result = tmp_sum

        return result


s = Solution()
print(s.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
