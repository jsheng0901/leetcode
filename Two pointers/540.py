from typing import List


class Solution1:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        线性搜索，每次条两步，如果当前数和下一个数不相等，说明找到出现频率为1的数，返回结果。
        """
        # 每次条两步的方式搜索
        for i in range(0, len(nums) - 2, 2):
            # 如果当前数和下一个数不相等，找到结果
            if nums[i] != nums[i + 1]:
                return nums[i]

        return nums[-1]


class Solution2:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Time O(log(n))
        Space O(1)
        二分法搜索，这里有个trick的地方是，如果一个数组都是两个数但是出现一次一个数，那么这个数组的长度一定是奇数，否则是偶数，利用这个特点来
        决定搜索mid那一边的subarray。详细见注释。
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            # 中位数
            mid = left + (right - left) // 2
            # 判断中位数左边的subarray不包含中位数自己的长度是否是偶数
            subarray_is_even = (right - mid) % 2 == 0

            # case1：中位数和右边的是双数
            if mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                # 不算中位数左边是偶数，说明算上中位数是奇数，target在右边，移动左指针两步
                if subarray_is_even:
                    left = mid + 2
                # 相反移动右指针一步
                else:
                    right = mid - 1
            # case2：中位数和左边的是双数
            elif mid > 0 and nums[mid] == nums[mid - 1]:
                # 不算中位数左边是偶数，因为和中位数相等的数在左边，那边中位数右边的已经是完整的偶数subarray了，
                # target在左边，移动右指针两步
                if subarray_is_even:
                    right = mid - 2
                # 相反移动左指针一步
                else:
                    left = mid + 1
            # case3：找到唯一一个两步都不相等的数也就是target，直接返回
            else:
                return nums[mid]

        # 特殊情况，但是其实走不到这里
        return nums[right]


class Solution3:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Time O(log(n))
        Space O(1)
        另一种二分法写法，因为我们知道如果都是成对的出现的话，我们只需要check偶数index和下一位index是否相等即可判断之前的subarray里面是否
        有单一数出现。保证我们每次都是check偶数index。
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            # 确保每次都是check偶数index
            mid = left + (right - left) // 2
            # 如果是奇数则 -1来保证check的是偶数index位置
            if mid % 2 == 1:
                mid -= 1
            # 如果当前数和下一个相等，说明前面所有subarray都是成对的出现，target在左边
            if mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                left = mid + 2
            # 如果不相等说明当前数是target或者在之前的subarray里面
            else:
                right = mid - 1

        # 出循环的时候是left = right + 1，所以当前target是left指针位置
        return nums[left]


s = Solution3()
print(s.singleNonDuplicate(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(s.singleNonDuplicate(nums=[3, 3, 7, 7, 10, 11, 11]))
