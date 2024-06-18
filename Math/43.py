class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Time O(m * n)
        Space O(m + n)
        题意是基础的两数相乘的数学题，但是这里涉及到让算法来实现。根据乘法顺序，从后向前相乘，每一步的乘积落在一个数组内，然后叠加，
        这里每一步落在数组内的index是最难的部分，其实 i * j 刚好落在 i + j 和 i + j + 1的两个index上。
        """
        m = len(num1)
        n = len(num2)
        # 结果最多为 m + n 位数
        res = [0] * (m + n)

        # 从个位数开始逐位相乘
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 当前乘积
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                # 乘积在 res 对应的索引位置
                p1, p2 = i + j, i + j + 1
                # 叠加到 res 上，先加p2后一位，因为可能有进位对于p1
                cur_sum = res[p2] + mul

                # 注意这里不能直接两个数叠加，因为题目不允许转化成int，先加后一位，然后再加前一位
                res[p2] = cur_sum % 10
                # 注意是叠加这里
                res[p1] += cur_sum // 10

        # 结果前缀可能存的 0（未使用的位）
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1

        # 将计算结果转化成字符串
        res_str = ''.join(str(e) for e in res[i:])

        # 结果可能是0
        return "0" if res_str == "" else res_str


s = Solution()
print(s.multiply(num1="2", num2="3"))
print(s.multiply(num1="123", num2="456"))
