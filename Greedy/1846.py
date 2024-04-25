from typing import List


class Solution1:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        """
        Time O(n * log(n))
        Space O(n)
        因为题目需要从1开始，又需要最大，那么我们从小到大排序后保证每次递增都可以取最大递增值1，如果当前数字可以decrease的话。
        如果不能decrease说明刚刚好相等和前一个数。每一步找最大值即可。
        """
        # 从小打到排序
        arr = sorted(arr)
        max_value = float('-inf')
        for i in range(len(arr)):
            # 如果初始值不是1，赋值1
            if i == 0 and arr[i] != 1:
                arr[i] = 1
            # 如果后续index和前一个相减大于1，说明可以decrease，赋值保证最大，所以 +1
            if i > 0 and abs(arr[i] - arr[i - 1]) > 1:
                arr[i] = arr[i - 1] + 1

            # 记录最大值
            max_value = max(max_value, arr[i])

        return max_value


class Solution2:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        """
        Time O(n * log(n))
        Space O(n)
        和思路1一模一样。但是其实我们并不需要赋值，只需要用一个指针一直track最大值即可，因为list的赋值其实隐藏了一个O(n)的操作。
        思路2的方法应该更快。理想状态应该是从1到n的一个递增序列，每个元素相差1。
        """
        # 同样从小打到排序
        arr = sorted(arr)
        # 最大值至少是1
        max_value = 1
        for i in range(1, len(arr)):
            # 如果当前值大于最大值 + 1，说明当前值可以decrease，说明我们的最大值可以增加1
            if arr[i] >= max_value + 1:
                max_value += 1

        return max_value


class Solution3:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        理论上我们并不需要sort，因为当给定长度的list时候，当前要求的条件下最优情况下的最大值应该就是list的长度，也就是n。
        我们记录每个数出现的频率。对于所有大于n的数我们一定会decrease当成n来记录。所以就有两种情况，
        第一种出现的数字需要的spot大于实际的spot，也就是 ans + counts[num] <= num，此时我们可以decrease出现的次数的spot
        第二种情况，刚好相反，出现的太多了大于需要的spot，那我们只能用需要的spot，也就是会出现很多一样的数字，此时最大值就是当前出现的这个数。
        """
        n = len(arr)
        counts = [0] * (n + 1)
        # 记录出现的频率，大于n的全部当做n来记录
        for num in arr:
            counts[min(num, n)] += 1

        ans = 1
        for num in range(2, n + 1):
            # 第一种情况，对应测试数据1
            if ans + counts[num] <= num:
                ans += counts[num]
            # 第二种情况，对应测试数据2
            else:
                ans = num

        return ans


s = Solution3()
print(s.maximumElementAfterDecrementingAndRearranging(arr=[1, 3, 3, 3, 3, 3, 3]))
print(s.maximumElementAfterDecrementingAndRearranging(arr=[1, 2, 3, 100, 100]))
