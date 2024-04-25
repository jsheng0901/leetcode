class Solution:
    def largestRectangleArea1(self, heights: [int]) -> int:
        """
        Time O(n)
        Space O(n)
        单调递减栈，栈头->栈尾从大到小, 当遇到当前元素小于栈顶元素的时候就开始计算面积，需要最小左边的index和最小右边index
        """
        heights.insert(0, 0)
        heights.append(0)
        stack = [0]
        result = 0
        for i in range(1, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:        # 开始计算面积
                tmp = stack[-1]
                stack.pop()
                if stack:           # 有可能没有左边的index，需要判断
                    min_right_index = i
                    min_left_index = stack[-1]
                    w = min_right_index - min_left_index - 1
                    h = heights[tmp]
                    result = max(result, w * h)
            stack.append(i)

        return result

    def largestRectangleArea2(self, heights: [int]) -> int:
        """
        三种情况分开写的方法，更直观
        找每个柱子左右侧的第一个高度值小于该柱子的柱子
        单调栈：栈顶到栈底：从大到小（每插入一个新的小数值时，都要弹出先前的大数值）
        栈顶，栈顶的下一个元素，即将入栈的元素：这三个元素组成了最大面积的高度和宽度
        情况一：当前遍历的元素heights[i]大于栈顶元素的情况
        情况二：当前遍历的元素heights[i]等于栈顶元素的情况
        情况三：当前遍历的元素heights[i]小于栈顶元素的情况
        """
        result = 0
        stack = [0]
        # 输入数组首尾各补上一个0（与42.接雨水不同的是，本题原首尾的两个柱子可以作为核心柱进行最大面积尝试）
        # 为什么要加元素0在结尾：
        # 如果数组本身就是升序的，例如[2,4,6,8]，那么入栈之后 都是单调递减，一直都没有走 情况三 计算结果的哪一步，所以最后输出的就是0了。
        # 为什么要加元素0在开头：
        # 如果数组本身是降序的，例如 [8,6,4,2]，在 8 入栈后，6 开始与8 进行比较，此时我们得到 mid（8），right（6），但是得不到 left。
        # 因为 将 8 弹出之后，栈里没有元素了，那么为了避免空栈取值，直接跳过了计算结果的逻辑。
        # 之后又将6 加入栈（此时8已经弹出了），然后 就是 4 与 栈口元素 6 进行比较，周而复始，那么计算的最后结果result就是0
        heights.insert(0, 0)
        heights.append(0)

        for i in range(1, len(heights)):
            # 情况一
            if heights[stack[-1]] < heights[i]:
                stack.append(i)
            # 情况二
            elif heights[stack[-1]] == heights[i]:
                stack.pop()
                stack.append(i)
            # 情况三
            else:
                # 抛出所有较高的柱子
                while stack and heights[stack[-1]] > heights[i]:
                    # 栈顶就是中间的柱子，此时需要计算面积的高度
                    top = stack.pop()
                    # 要判断一下是否栈存在的原因是要找到当前栈顶最左边的元素来计算宽度，如果不判断，则对于单调递减的list，宽度永远是1
                    # 比如：[8, 6, 4, 2]，不判断的话，永远长方形宽度是1。
                    if stack:
                        left = stack[-1]
                        h = heights[top]
                        # 此处计算宽度的方式必须要最小左边的index，最小右边index和当前栈顶元素，因为有[1,1]这种情况
                        w = i - left - 1
                        result = max(result, h * w)

                stack.append(i)

        return result

