class Solution:
    def longestSubarray(self, nums: [int], limit: int) -> int:
        """
        两个deque控制单调性, 一个单调递减，一个单调递增，同时找到当前区间内最大差值，如果小于等于limit，就对比记录最大长度
        如果不满足limit, 则移动left pointer直到下一个满足的index
        :param nums:
        :param limit:
        :return:
        """
        left = 0
        right = 0
        result = 0

        deque_max = []
        deque_min = []

        while right < len(nums):
            while len(deque_max) > 0 and deque_max[-1] < nums[right]:   # 单调递减deque
                deque_max.pop()
            while len(deque_min) > 0 and deque_min[-1] > nums[right]:   # 单调递增deque
                deque_min.pop()

            deque_max.append(nums[right])
            deque_min.append(nums[right])

            while deque_max[0] - deque_min[0] > limit:  # 不满足则移动left
                if deque_max[0] == nums[left]:          # 移动前check第一个是不是要删除的元素，如果第一个刚好是left对应的元素
                    deque_max.pop(0)
                elif deque_min[0] == nums[left]:        # 同上
                    deque_min.pop(0)

                left += 1                               # 移动left

            result = max(result, right - left + 1)      # 记录最长距离
            right += 1

        return result
