class Solution:
    def select(self, left, right, k, nums):
        if left == right:
            return nums[left]

        # select a random pivot_index between
        pivot_index = left

        # find the pivot position in a sorted list
        pivot_index = self.partition(left, right, pivot_index, nums)

        # the pivot is in its final sorted position
        if k == pivot_index:
            return nums[k]
        # go left
        elif k < pivot_index:
            return self.select(left, pivot_index - 1, k, nums)
        # go right
        else:
            return self.select(pivot_index + 1, right, k, nums)

    def partition(self, left, right, pivot_index, nums):
        pivot = nums[pivot_index]

        # 1. move pivot to end, to make sure all
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        # 2. move all smaller elements to the left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # 3. move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]

        return store_index

    def findKthLargest(self, nums: [int], k: int) -> int:
        """
        1. 在数组区间随机取 pivot index = left + random[right-left] .
        2. 根据pivot 做 partition，在数组区间，把小于pivot的数都移到pivot左边。
        3. 得到pivot的位置 index，compare(index, (n-k)).
            a. index == n-k -> 找到第`k`大元素，直接返回结果。
            b. index < n-k -> 说明在`index`右边，继续找数组区间`[index+1, right]`
            c. index > n-k -> 那么第`k`大数在`index`左边，继续查找数组区间`[left, index-1]`.
        """

        return self.select(0, len(nums) - 1, len(nums) - k, nums)
