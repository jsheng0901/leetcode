class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        """
        Time O(n)
        Space O(1)
        从后往前遍历，如果是9则变成1，然后继续向前遍历，如果不是9则说明我们遇到了可以叠加的位置，+1后赋值并直接返回结果，不再需要继续遍历。
        """
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = (digits[i] + 1) % 10
            # 如果某一位不是0，则直接返回digital，说明我们已经在上面 +1 结束了
            if digits[i] != 0:
                return digits

        # 走到这说明都是9，加完后全都是0，然后直接加一个1在最前面
        digits.insert(0, 1)

        return digits


s = Solution()
print(s.plusOne(digits=[9, 9, 9]))
