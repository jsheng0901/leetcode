class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = (digits[i] + 1) % 10
            # 如果某一位不是0，则直接返回digital
            if digits[i] != 0:
                return digits

        digits.insert(0, 1)  # 如果全都是0，则直接加一个1在最前面

        return digits


s = Solution()
print(s.plusOne(digits=[9, 9, 9]))
