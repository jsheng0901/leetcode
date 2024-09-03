from typing import List


class Solution1:
    def left_bound_search(self, left, right, nums, target):

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1

        return left

    def triangleNumber(self, nums: List[int]) -> int:
        """
        Time O(n * log(n) + n^2 * log(n))
        Space O(1)
        Python里面sort是in-place的，不占据额外空间。此题有好几个思路，如果我们固定两条边，那么我们需要找到第三条边小于另外两条边的和。
        先sort一下，保证有序查找，找到第三条边的bound，小于这个bound的都可以直接叠加计算个数，找bound因为在有序数组内查找，可以使用二分法。
        """
        count = 0
        nums.sort()

        # 固定两条边
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # target值，也就是第三条边不能比这个值大
                target = nums[i] + nums[j]
                # 找到这个值对应的左边界，也就是取不到这个值的最小index
                left_bound_index = self.left_bound_search(j + 1, len(nums) - 1, nums, target)
                # 计算这个边界内所有的符合条件的个数 (k - 1) - (j + 1) - 1 = k - j - 1
                count += left_bound_index - j - 1

        return count


class Solution2:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        Time O(n * log(n) + n^3)
        Space O(1)
        同样的固定两条边的思路，只是这里我们可以线性搜索符合k的个数，但是有个优化，因为是有序数组，当我们移动j指针的时候，我们并不需要从
        k = j + 1开始查找，完全可以从上一次合理的k开始查找，因为j变大了，之前符合条件的k一定都继续符合条件，用一个指针记录之前找到合理的k。
        详细见注释，有些特殊情况需要考虑进去。
        """
        count = 0
        nums.sort()
        prev_k = None
        # 固定两条边
        for i in range(len(nums)):
            # 每次初始化一下前一个k的值
            # prev_k = None
            for j in range(i + 1, len(nums)):
                # 如果没有值，或者前一个完全没有找到符合的k，从新赋值k
                if prev_k is None or prev_k <= j:
                    k = j + 1
                else:
                    # 如果有前一个符合的k，从上一个k开始遍历，直接先叠加上一个的部分个数
                    k = prev_k
                    count += prev_k - j - 1

                # 满足符合条件的k，就继续叠加并移动k
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    count += 1
                    k += 1
                # 复制新的前一个k指针
                prev_k = k

        return count


class Solution3:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        Time O(n * log(n) + n^2)
        Space O(1)
        换个思路，每次我们可以固定一个指针，贪心的思路，从最大边开始，找两条边的和大于最大边的数个。如果两条边的和小于，则移动左指针，如果大于
        说明找到了合理的区间，叠加个数同时移动右指针。
        """
        nums.sort()
        count = 0
        # 反向遍历固定最大的边
        for k in range(len(nums) - 1, -1, -1):
            # 左右指针
            i = 0
            j = k - 1
            # 找到合理区间
            while i < j:
                # 如果符合条件，说明 [i, j] 里面所有的点都符合条件，因为是递增数组
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                # 如果小于等于，移动左指针，增大区间值
                else:
                    i += 1

        return count


s = Solution2()
print(s.triangleNumber(nums=[2, 2, 3, 4]))
print(s.triangleNumber(nums=[7, 0, 0, 0]))
print(s.triangleNumber(nums=[1, 1, 3, 4]))
print(s.triangleNumber(nums=[24, 3, 82, 22, 35, 84, 19]))
