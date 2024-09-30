class Solution1:
    def intToRoman(self, num: int) -> str:
        """
        Time O(1)
        Space O(1)
        应该算是一道数学题，把所有的罗马数字对应阿拉伯数字映射起来，然后从最大的开始遍历，一次找到对应的罗马数字。
        """
        # 存储映射关系
        digits = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        roman_digits = []
        # 从大到小遍历
        for value, symbol in digits:
            # 如果没有数字了，说明遍历完了
            if num == 0:
                break
            # 找到对应的除之后的结果，和对应的余数
            count, num = divmod(num, value)
            # 加入结果
            roman_digits.append(symbol * count)

        # 连接起来
        return "".join(roman_digits)


class Solution2:
    def intToRoman(self, num: int) -> str:
        """
        Time O(1)
        Space O(1)
        同样的思路，从千位到各位一次进行对应查找，出现的频率就是对应位置的index。
        """
        # 列出来千位到各位的罗马数字，出现的频率就是index
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        # 计算每个位置出现的频率，并连接起来结果
        return (
                thousands[num // 1000]
                + hundreds[num % 1000 // 100]
                + tens[num % 100 // 10]
                + ones[num % 10]
        )


s = Solution2()
print(s.intToRoman(num=3749))
print(s.intToRoman(num=58))
