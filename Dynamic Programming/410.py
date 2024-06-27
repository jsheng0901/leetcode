from typing import List


class Solution:
    def dp(self, nums, start_index, subarray_count, memo):
        # 如果只剩下一个subarray，说明剩下的所有数组组成一个subarray
        if subarray_count == 1:
            # 返回剩下这个subarray的总和
            return sum(nums[start_index:])

        # 如果备忘录中出现过，直接返回结果
        if memo[start_index][subarray_count] != -1:
            return memo[start_index][subarray_count]

        # 记录当前start index对应的k的状态下的最小最大subarray总和
        min_largest_split_sum = float('inf')
        # 开始遍历start index开始到最后的所有可能切分点
        for i in range(start_index, len(nums) - subarray_count + 1):
            # 第一组subarray
            first_split_sum = sum(nums[start_index: i + 1])
            # 剩下的subarray的返回值，递归接住，后续遍历思路。注意start index要 +1，同时少了一个subarray
            second_split_sum = self.dp(nums, i + 1, subarray_count - 1, memo)
            # 计算最大的 subarray 总和对于当前 i 这个位置切分后的结果
            largest_split_sum = max(first_split_sum, second_split_sum)
            # 对于每一组切分点找到最小的 subarray 总和
            min_largest_split_sum = min(min_largest_split_sum, largest_split_sum)

            # 优化思路，如果第一组切分已经大于当前最小值的情况下，不用在继续找切分组合了，因为此时最小情况已经找到
            if first_split_sum >= min_largest_split_sum:
                break
        # 记录进备忘录
        memo[start_index][subarray_count] = min_largest_split_sum

        # 返回当前状态对应的结果
        return min_largest_split_sum

    def splitArray(self, nums: List[int], k: int) -> int:
        """
        Time O(n * m * n)
        Space O(n * m)
        DP的思想来做，两个状态，分别是当前切割的index和当前还剩下多少subarray要切分。时间复杂度上对于所有状态我们都需要遍历一次
        start index到 n - subarray count的loop，所以是 n * m * n。详细思路见注释。但是这里计算subarray的时候我们用的是sum，明显
        是多一个O(n)的操作，虽然可以过所有test case但是很慢。
        """
        # 构建备忘录，记得备忘录是 n * k 的大小不要弄反了
        memo = [[-1] * (k + 1) for _ in range(len(nums))]

        return self.dp(nums, 0, k, memo)


class Solution2:
    def dp(self, nums, start_index, subarray_count, memo, pre_sum):
        if subarray_count == 1:
            # 区别在这里，计算subarray的总和的时候用前缀和直接相减
            return pre_sum[len(nums)] - pre_sum[start_index]

        if memo[start_index][subarray_count] != -1:
            return memo[start_index][subarray_count]

        # 区别在这里，计算subarray的总和的时候用前缀和最后一位
        min_largest_split_sum = pre_sum[len(nums)]
        for i in range(start_index, len(nums) - subarray_count + 1):
            # 区别在这里，计算subarray的总和的时候用前缀和对应的index直接相减
            first_split_sum = pre_sum[i + 1] - pre_sum[start_index]
            second_split_sum = self.dp(nums, i + 1, subarray_count - 1, memo, pre_sum)
            largest_split_sum = max(first_split_sum, second_split_sum)

            min_largest_split_sum = min(min_largest_split_sum, largest_split_sum)

            if first_split_sum >= min_largest_split_sum:
                break

        memo[start_index][subarray_count] = min_largest_split_sum

        return min_largest_split_sum

    def get_pre_sum(self, nums):
        # 前缀和数组
        pre_sum = [0] * (len(nums) + 1)
        # 计算 nums 的累加和
        for i in range(1, len(pre_sum)):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        return pre_sum

    def splitArray(self, nums: List[int], k: int) -> int:
        """
        Time O(n * m * n)
        Space O(n * m)
        一模一样的思路，但是计算subarray的总和的时候我们用前缀和的思路来计算，保证每次计算subarray总和都是O(1)的操作。
        """
        memo = [[-1] * (k + 1) for _ in range(len(nums))]
        # 计算前缀和
        pre_sum = self.get_pre_sum(nums)

        return self.dp(nums, 0, k, memo, pre_sum)


class Solution3:
    def min_subarrays_required(self, nums, max_sum_allowed):
        # 单调递减函数，对于给定的最大值和subarray个数之间的关系
        current_sum = 0
        splits_required = 0

        for element in nums:
            # Add element only if the sum doesn't exceed max_sum_allowed
            if current_sum + element <= max_sum_allowed:
                current_sum += element
            else:
                # If the element addition makes sum more than max_sum_allowed
                # Increment the splits required and reset sum
                current_sum = element
                splits_required += 1

        # Return the number of subarray, which is the number of splits + 1
        return splits_required + 1

    def splitArray(self, nums: List[int], k: int) -> int:
        """
        Time O(n * log(s))  s --> sum of nums, binary search range
        Space O(1)
        此题可以用二分法来做，换个角度思考，我们去猜当给定一个最大值的结果的时候需要最少多少个subarray，这里有个关系是，当我们给定的这个结果
        越小的时候，我们需要的subarray也就越多，相反给定的越大的时候，需要的subarray也就更少，也就是说我们这里存在一个单调递减的函数关系，
        搜索空间是有序的，那么我们一定可以执行二分法来搜索。详细见注释。此题整体逻辑和1011一模一样。
        """
        # 最小情况是subarray是单个数
        left = max(nums)
        # 最大情况是subarray是整个nums
        right = sum(nums)

        while left <= right:
            # 中间点
            mid = left + (right - left) // 2
            # 找到最少需要的subarray个数
            num_subarray = self.min_subarrays_required(nums, mid)
            # 小于等于都是移动右指针，因是单调递减函数，找左边界写法
            if num_subarray < k:
                right = mid - 1
            elif num_subarray == k:
                right = mid - 1
            # 大于则移动左指针
            elif num_subarray > k:
                left = mid + 1

        return left


s = Solution3()
print(s.splitArray(nums=[7, 2, 5, 10, 8], k=2))
print(s.splitArray(nums=[1, 2, 3, 4, 5], k=2))
print(s.splitArray(nums=[1, 4, 4], k=3))
