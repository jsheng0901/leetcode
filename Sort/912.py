from random import randint


class Solution1:
    """quick sort"""
    def sortArray(self, nums: [int]) -> [int]:

        def partition(nums, left, right):
            if left > right:
                return

            pivot_index = left

            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            store_index = left
            for i in range(left, right):
                if nums[i] < nums[right]:
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1

            nums[store_index], nums[right] = nums[right], nums[store_index]

            partition(nums, left, store_index - 1)
            partition(nums, store_index + 1, right)

            return

        partition(nums, 0, len(nums) - 1)

        return nums


class Solution2:
    """quick sort another edition, make sure use randint, otherwise can't pass long array"""
    def partition(self, nums, left, right):

        pivot_index = randint(left, right)

        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        store_index = left
        for i in range(left, right):
            if nums[i] < nums[right]:
                nums[i], nums[store_index] = nums[store_index], nums[i]
                store_index += 1

        nums[store_index], nums[right] = nums[right], nums[store_index]

        return store_index

    def quick_sort(self, nums, left, right):
        if left < right:
            pivot_index = self.partition(nums, left, right)
            self.quick_sort(nums, left, pivot_index - 1)
            self.quick_sort(nums, pivot_index + 1, right)

        return nums

    def sortArray(self, nums: [int]) -> [int]:

        return self.quick_sort(nums, 0, len(nums) - 1)


s = Solution2()
print(s.sortArray(nums=[5, 1, 1, 2, 0, 0]))
