class Solution:
    def largestSumAfterKNegations(self, A: [int], K: int) -> int:
        """
        第一步：将数组按照绝对值大小从大到小排序，「注意要按照绝对值的大小」
        第二步：从前向后遍历，遇到负数将其变为正数，同时K--
        第三步：如果K还大于0，那么反复转变数值最小的元素，将K用完
        第四步：求和
        :param A:
        :param K:
        :return:
        """
        A = sorted(A, key=abs)  # 第一步
        A = A[::-1]
        for i in range(len(A)):
            if A[i] < 0 and K > 0:
                A[i] *= -1
                K -= 1

        while K > 0:
            A[-1] *= -1
            K -= 1

        result = sum(A)

        return result


s = Solution()
print(s.largestSumAfterKNegations(A=[4, 2, 3], K=1))
