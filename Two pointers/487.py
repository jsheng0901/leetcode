from typing import List


class Solution1:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        借用最大岛屿的方法，只是放在一维空间上。统计出所有连续1的端点对应的此时连续1的长度，并存在map里面，key是index，value是长度。
        逐一遍历0的位置，根据不同的7种情况统计处反转后最长长度是多少，记录最长的情况。
        """
        num1_2_size = {}
        first_flag = False
        left = 0
        tmp = 0
        result = 0

        for i in range(len(nums)):
            # 遇到1，并且没有起点
            if nums[i] == 1 and first_flag is False:
                left = i
                first_flag = True
            # 遇到1并且有起点
            if nums[i] == 1 and first_flag:
                tmp += 1
            # 遇到0，并且有起点，说明可以结束起点，开始新的起点
            if nums[i] == 0 and first_flag:
                first_flag = False
                num1_2_size[left] = tmp
                num1_2_size[i - 1] = tmp
                result = max(result, tmp)
                tmp = 0

        if tmp > 0:
            num1_2_size[left] = tmp
            num1_2_size[len(nums) - 1] = tmp
            result = max(result, tmp)

        for i in range(len(nums)):
            if nums[i] == 0:
                # 分别对应7种情况的0，计算可能最长的1的subarray
                if i > 0 and nums[i - 1] == 1:
                    result = max(result, 1 + num1_2_size[i - 1])
                if i < len(nums) - 1 and nums[i + 1] == 1:
                    result = max(result, 1 + num1_2_size[i + 1])
                if 0 < i < len(nums) - 1 and nums[i - 1] == 1 and nums[i + 1] == 1:
                    result = max(result, 1 + num1_2_size[i - 1] + num1_2_size[i + 1])
                if i > 0 and nums[i - 1] != 1:
                    result = max(result, 1)
                if i < len(nums) - 1 and nums[i + 1] != 1:
                    result = max(result, 1)
                if 0 < i < len(nums) - 1 and nums[i - 1] != 1 and nums[i + 1] != 1:
                    result = max(result, 1)
                if i == 0 and len(nums) == 1:
                    result = max(result, 1)

        return result


class Solution2:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        和1004一模一样，只是此时的k等于1
        """
        window = 0
        left = 0
        right = 0
        result = 0

        while right < len(nums):
            # 需要被加进来的元素
            c = nums[right]
            # 下一个右指针位置
            right += 1
            # 更新窗口内0的出现次数
            if c == 0:
                window += 1

            # 判断窗口是否需要收缩
            while window > 1:
                # 需要踢出去的元素
                d = nums[left]
                # 下一个左指针位置
                left += 1
                # 更新窗口内0的出现次数
                if d == 0:
                    window -= 1
            # 更新当前最长距离，这里不用 +1，因为右指针已经往前跳了一步
            result = max(result, right - left)

        return result


s = Solution2()
print(s.findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0]))
