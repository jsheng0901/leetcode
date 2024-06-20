class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        Time O(n)
        Space O(n)
        此题逻辑：
        1. 找到第一个下降点，下降低的意义是从后往前第一个index + 1大于 index的点。
        2. 再从后往前在index的右边找到第一个大于下降点的数的index，swap这两个数。
        3. 然后把下降点后所有数字收尾swap，因为从后向前遍历当遇到不是递增的第一个下降点的时候此时后面这一部分序列已经是递减的顺序了，
           所以最后直接reverse就是递增的序列
        此题和31题一模一样的逻辑，只是这里多了两个限制，一个是如果找不到直接返回 -1，另一个是如果大于32位直接返回 -1。
        """
        # 转化成 list of int 方便后续比大小，这里也是唯一的额外空间使用
        # 下面逻辑和31一模一样
        nums = [int(i) for i in str(n)]
        down_index = None
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                down_index = i
                break

        if down_index is None:
            return -1

        for i in range(len(nums) - 1, -1, -1):
            if nums[down_index] < nums[i]:
                nums[down_index], nums[i] = nums[i], nums[down_index]
                break

        i, j = down_index + 1, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        # 到这里我们只需要再把所有数字转化成string，然后最后转化成int再对比即可
        res = ''
        for i in nums:
            res += str(i)

        # 注意转化成int，并且对比 32-bit integer
        return int(res) if int(res) < 2 ** 31 else -1


s = Solution()
print(s.nextGreaterElement(n=12))
print(s.nextGreaterElement(n=21))
print(s.nextGreaterElement(n=5719))
print(s.nextGreaterElement(n=2147483486))
