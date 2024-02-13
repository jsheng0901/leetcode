from typing import List


class Solution1:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        Time O(n)
        Space O(1)
        线性搜索，找到两个数字之前缺失的个数，如果确实的个数等于K，则说明K在这两个数之间。则直接返回。
        """
        # if the kth missing is less than arr[0]
        if k <= arr[0] - 1:
            return k
        k -= arr[0] - 1

        # search kth missing between the array numbers
        for i in range(len(arr) - 1):
            # missing between arr[i] and arr[i + 1]
            curr_missing = arr[i + 1] - arr[i] - 1
            # if the kth missing is between
            # arr[i] and arr[i + 1] -> return it
            if k <= curr_missing:
                return arr[i] + k
            # otherwise, proceed further
            k -= curr_missing

        # if the missing number is greater than arr[-1]
        return arr[-1] + k


class Solution2:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        Time O(n)
        Space O(1)
        双指针写法，同时遍历两个数组，一个是arr，一个是正常的n个数的array。然后找missing number个数，如果meeting了K，则说明不用再找了，
        直接返回结果。
        """
        p1 = 0
        p2 = 1
        miss_number = 0

        while p2:
            # 如果当前arr和时间应该的数不等的时候，说明找到一个missing number
            if p2 != arr[p1]:
                miss_number += 1
                # 如果等于K，则直接返回
                if miss_number == k:
                    return p2
            else:
                # 如果arr没有走完，并且遇到了相等的数，arr指针向前走
                if p1 < len(arr) - 1:
                    p1 += 1
            # 每次更新正常数组的指针
            p2 += 1


class Solution3:
    def findKthPositive(self, arr: [int], k: int) -> int:
        """
        Time O(log(n))
        Space O(1)
        二分法搜索，这里有个终点是如何找到当前index对应的缺失个数是多少。另一个重点是出循环的时候是 left = right + 1，
        arr[right] + k - (arr[right] - right - 1) 表示当前右指针对应的缺失的K的个数在减掉已经在右指针用完的个数，就是我们要找的数。
        """
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            # arr[mid] - mid - 1 表示当前index对应的数缺失了多少个数
            # 如果缺失的少于K，说明还需要找到更大的数
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            # 反之找更小的数
            else:
                right = mid - 1

        return left + k


s = Solution2()
print(s.findKthPositive(arr=[2, 3, 4, 7, 11], k=5))
