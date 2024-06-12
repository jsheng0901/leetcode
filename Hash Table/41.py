from typing import List


class Solution1:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        用一个数组来记录是否见过此数字，注意这里数字在 1 - n 之间的数字才会被记录下来，其它数字直接跳过。再遍历记录数组，第一个没有见过的就是
        我们需要的结果，如果都见过，说明缺失的是 n + 1 这个数。
        """
        n = len(nums)
        seen = [False] * (n + 1)  # Array for lookup

        # Mark the elements from nums in the lookup array
        for num in nums:
            if 0 < num <= n:
                seen[num] = True

        # Iterate through integers 1 to n
        # return smallest missing positive integer
        for i in range(1, n + 1):
            if not seen[i]:
                return i

        # If seen contains all elements 1 to n
        # the smallest missing positive number is n + 1
        return n + 1


class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        核心思想和442，448一样，用数组本身作为hash map来记录是否出现过，只是这里因为数组内存在负数和0的情况，我们不能使用 * -1 这种操作
        来记录是否出现过。需要考虑cycle sort，核心思想就是，对于在 1 - n 之间的数，正确的index应该是 num - 1，比如也就是 4 应该在 3
        这个 index 上。所以对于这个数我们可以找到正确的位置并放置，最后遍历找到 index + 1 和数字不一样的index，第一个出现的就是结果。
        同理都没有的话就是 n + 1。
        """
        n = len(nums)
        i = 0
        # Use cycle sort to place positive elements smaller than n
        # at the correct index
        # 这里用while loop，因为我们swap完后，还要继续判断swap过来的数
        while i < n:
            # 正确的index
            correct_index = nums[i] - 1
            # 如果数在 1 - n 直接，并且不在正确的位置上，进行swap
            if 0 < nums[i] <= n and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            # 如果不符合条件，比如大于数组长度，比如是负数，跳过
            else:
                i += 1

        # 找到第一个不匹配的数
        for i, val in enumerate(nums):
            if val != i + 1:
                # 注意是返回 index + 1
                return i + 1

        # 如果都匹配，说明正确的位置上都有数，结果只能是没有包括进来的数 n + 1
        return n + 1


s = Solution2()
print(s.firstMissingPositive(nums=[3, 4, -1, 1]))
print(s.firstMissingPositive(nums=[1]))
print(s.firstMissingPositive(nums=[7, 8, 9, 11, 12]))
print(s.firstMissingPositive(nums=[1, 2, 0]))
