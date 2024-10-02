from typing import List


class Solution1:
    def validSubarrays(self, nums: List[int]) -> int:
        """
        Time O(n^2)
        Space O(1)
        此题很有意思，因为暴力方法也可以过所有test。很简单的思路，直接两loop，遇到合理的就 +1，不合理的直接结束内层循环。
        """
        result = 0
        for i in range(len(nums)):
            path = [nums[i]]
            # 如果要记录具体的subarray，就在这记录，记得copy path list进result前，不然会随着改变而改变result里面的结果
            # result.append(path[:])
            # 遇到一个合理的subarray
            result += 1
            # 记录最左的数字
            left_most = nums[i]
            for j in range(i + 1, len(nums)):
                # 合理的subarray
                if nums[j] >= left_most:
                    path.append(nums[j])
                    # result.append(path[:])
                    result += 1
                # 不合理，直接结束内层循环，开始新的subarray
                else:
                    break

        return result


class Solution2:
    def validSubarrays(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        单调栈的思路，因为我们需要每个subarray的第一个元素是整个array最小的元素，所以我们可以找每个元素下一个小于它的元素的index。对于没有
        下一个小于它的元素的index应该是整个array的长度，有多少个subarray在下一个小于它的元素和这个元素之间，
        其实很简单应该是下一个的index - 当前index，这里因为下一个更小的index不考虑在subarray内，所以直接相减，不然个数要 + 1。详细见注释。
        """
        n = len(nums)
        # 构建下一个更小的数组，初始值是array的长度，如果没有下一个更小的数的时候
        next_small = [n] * n
        stack = []

        for i in range(len(nums)):
            # 如果当前栈顶元素大于当前元素，说明要弹出栈顶元素，达到单调递增栈（栈底 -> 栈顶）递增
            while stack and nums[stack[-1]] > nums[i]:
                # 给当前弹出的元素对应的下一个更小array数组赋值当前index
                next_small[stack.pop()] = i
            # 入栈
            stack.append(i)

        result = 0
        # 遍历整个下一个最小的数组，可组成的subarray个数就是两个index的差值
        for i in range(len(next_small)):
            result += next_small[i] - i

        return result


class Solution3:
    def validSubarrays(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        一模一样的思路和解法2，不过可以更简便，减少了遍历整个下一个更小数组的遍历，详细见注释。
        """
        n = len(nums)
        stack = []
        result = 0

        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                # 当前弹出的index和当前index的差值就是此时subarray的个数，直接在这里弹出的加入结果
                result += i - stack.pop()
            stack.append(i)

        # 如果还有元素在里面，此时都是没有下一个最小的元素，也就是array长度是最长的index
        while stack:
            result += n - stack.pop()

        return result


s = Solution2()
print(s.validSubarrays(nums=[1, 4, 2, 5, 3]))
