from typing import List


class Solution:
    def trap1(self, height: [int]) -> int:
        """
        Time O(n)
        Space O(n)
        从小到大的顺序（从栈头到栈底），单调递增stack，
        当前数字小于stack top数字时候加入stack，遇到当前数字更大的时候，弹出top，计算此时水量，
        这里计算水量要引入弹出后的top，找到最矮的高度，计算宽度，用stack里面加入的index计算。
        通过三个元素来接水：栈顶，栈顶的下一个元素，以及即将入栈的元素，
        雨水高度是 min(凹槽左边高度, 凹槽右边高度) - 凹槽底部高度，
        雨水的宽度是 凹槽右边的下标 - 凹槽左边的下标 - 1（因为只求中间宽度）。
        """
        if len(height) < 3:
            return 0

        stack = []
        result = 0

        for i in range(len(height)):
            while len(stack) > 0 and height[stack[-1]] < height[i]:  # 当前数字大于top数字
                top = stack.pop()  # 弹出top

                while len(stack) > 0 and height[top] == height[stack[-1]]:  # 如果前一个一模一样，继续弹出top
                    stack.pop()

                if len(stack) > 0:
                    tmp_top = height[stack[-1]]  # 弹出后的top
                    h = min(tmp_top - height[top], height[i] - height[top])  # 弹出后形成的最矮高度
                    w = i - stack[-1] - 1
                    result += h * w

            stack.append(i)

        return result

    def trap2(self, height: [int]) -> int:
        """
        第二种写法，三种情况更清晰：
        情况一：当前遍历的元素（柱子）高度小于栈顶元素的高度
        情况二：当前遍历的元素（柱子）高度等于栈顶元素的高度
        情况三：当前遍历的元素（柱子）高度大于栈顶元素的高度
        """
        stack = [0]
        result = 0

        for i in range(1, len(height)):
            if height[i] < height[stack[-1]]:           # 情况1
                stack.append(i)
            elif height[i] == height[stack[-1]]:        # 情况2
                stack.pop()
                stack.append(i)
            else:
                while stack and height[i] > height[stack[-1]]:      # 情况3
                    top = stack.pop()
                    while stack and height[stack[-1]] == height[top]:
                        stack.pop()

                    if len(stack) > 0:
                        cur_top = stack[-1]
                        h = min(height[cur_top], height[i]) - height[top]
                        w = i - cur_top - 1
                        result += h * w
                stack.append(i)

        return result


class Solution3:
    def trap(self, height: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        双指针写法，这里一边遍历一遍计算。trap的区域只需要考虑当前的最底高度和当前高度的差，也就是 min(l_max, r_max)
        至于l_max和r_max是不是当前i的左右最高并不重要。详细见注释。
        参考 https://labuladong.online/algo/frequency-interview/trapping-rain-water/
        """
        left = 0
        right = len(height) - 1
        l_max = 0
        r_max = 0
        res = 0
        while left < right:
            # 左边最大的高度 height[0..left]
            l_max = max(l_max, height[left])
            # 右边最大的高度 height[right..end]
            r_max = max(r_max, height[right])
            # 当前左边已经比右边更小了，也就是高度选择和l_max有关系，至于r_max是不是i右边的最高高度不重要
            if l_max < r_max:
                # 当前高度差，这里底永远是1，所以不用 h * w
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1

        return res


s = Solution()
print(s.trap2(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
