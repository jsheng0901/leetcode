class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: [int], verticalCuts: [int]) -> int:
        """
        O(N⋅log(N)+M⋅log(M)) time, O(1) space, 姑且算贪心，横轴纵轴局部最大，总体面积最大
        先加入起始和结尾，然后sort切割点，计算最大间隔区间，同理对横纵轴
        """
        h_max = float('-inf')
        v_max = float('-inf')
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        horizontalCuts.sort()
        verticalCuts.sort()

        for i in range(1, len(horizontalCuts)):
            h_max = max(h_max, horizontalCuts[i] - horizontalCuts[i - 1])

        for i in range(1, len(verticalCuts)):
            v_max = max(v_max, verticalCuts[i] - verticalCuts[i - 1])

        return (h_max * v_max) % (10 ** 9 + 7)      # 记得要除以这个除数取余数


