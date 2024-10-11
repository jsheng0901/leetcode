from typing import List


class Solution1:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        Time O(n * log(n))
        Space O(1)
        首先最大的三个数的乘积，只会有三种情况，本质上是负数的个数，两种情况第一种全都正数，第二种一正两负
        case1: 最大的三个数相乘，对应全正数
        case2: 最大的数乘以最小的两个数，对应一正两负
        case3: 最大的数乘以第二大的数乘以最小的数，对应一正两负
        我们可以先sort一下，这样能快速找到我们需要的五个数，然后分别计算三种情况取最大值。
        """
        # 先sort
        nums.sort()

        # 三种情况
        case1 = nums[-1] * nums[-2] * nums[-3]
        case2 = nums[-1] * nums[0] * nums[1]
        case3 = nums[-1] * nums[-2] * nums[0]

        # 取最大值
        res = max(case1, case2, case3)

        return res


class Solution2:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        一模一样的思路，但是我们其实可以不需要sort整个数组，因为我们只需要五个数，完全可以遍历一次数组，找到这五个数即可，
        用五个指针来找到这五个数。
        """
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        min1, min2 = float('inf'), float('inf')

        for num in nums:
            # 找最大值
            if num >= max1:
                # 一定要先赋值，否则会丢失之前的最值
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2:
                max3 = max2
                max2 = num
            elif num >= max3:
                max3 = num

            # 找最小值
            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num

        case1 = max1 * max2 * max3
        case2 = max1 * min1 * min2
        case3 = max1 * max2 * min1

        res = max(case1, case2, case3)

        return res


s = Solution2()
print(s.maximumProduct(nums=[1, 2, 3]))
print(s.maximumProduct(nums=[1, 2, 3, 4]))
print(s.maximumProduct(nums=[-1, -2, -3]))
