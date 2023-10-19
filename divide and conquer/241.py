from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
        Time O(卡特兰数)
        Space O(n)
        经典分治题型，当原问题可以分解成小规模的子问题，然后根据子问题的结果构造出原问题的答案。此时说明题目可以用分治的思想，
        可以理解为一直算法思路，类似动态规划的子问题推导最终结果。
        此题可以不要思考整体，而是把目光聚焦局部，只看一个运算符。当我们以运算符号进行拆分原始问题时候，类似一颗二叉树一直进行左右拆分，
        遇到运算符号就拆分，直到走到底也就是没有运算符号的时候，此时返回数字本身，类似后续遍历的思路，当我们拿到左右节点的返回值的时候，
        我们在中间节点进行，拆分输入string的时候遇到的运算符号的真正运算，这里需要遍历所有左右节点返回值的组合结果。
        ex: 当前节点是 - 符号，当前节点的输入string是 "2 - 1"，左右节点分别返回 [2]，[1]，我们需要运算的是 2 - 1 = 1，返回 [1]。
        不需要考虑整体到底干啥，只需要直到当前节点和左右节点到底在干啥，最终递归函数会返回所有结果。分治题目主要考虑两个点：
        1. 不要思考整体，而是把目光聚焦局部
        2. 明确递归函数的定义是什么，相信并且利用好函数的定义
        此题还可以带一个备忘录进行减枝，因为递归的过程中会遇到已经算过的string组合，此时我们只需要每次记录当前string的返回结果进备忘录就行。
        """
        # 避免重复计算
        if expression in self.memo:
            return self.memo[expression]

        res = []

        # 扫描算式 expression 中的运算符
        for i in range(len(expression)):
            c = expression[i]
            if c in ['-', '*', '+']:
                # 以运算符为中心，分割成两个字符串，分别递归计算
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                # 通过子问题的结果，合成原问题的结果
                for l in left:
                    for r in right:
                        if c == "+":
                            res.append(l + r)
                        elif c == "-":
                            res.append(l - r)
                        elif c == "*":
                            res.append(l * r)

        # base case
        # 如果 res 为空，说明算式是一个数字，没有运算符
        # 这里不能通过长度判断输入进来的是不是没有运算符，因为长度可能是一个数字也可能是两个数组。ex: "1", "11"
        if not res:
            res.append(int(expression))

        # 将结果添加进备忘录
        self.memo[expression] = res

        return res


s = Solution()
print(s.diffWaysToCompute(expression="2-1-1"))
print(s.diffWaysToCompute(expression="11"))
