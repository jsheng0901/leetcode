class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """whole idea is add from back and use carry to remember 进位"""
        carry = 0

        p1 = len(num1) - 1
        p2 = len(num2) - 1
        result = []

        while p1 >= 0 or p2 >= 0 or carry != 0:
            curr = carry

            if p1 >= 0:
                curr += int(num1[p1])
            if p2 >= 0:
                curr += int(num2[p2])

            if curr <= 9:
                result.append(curr)
                carry = 0
            else:
                result.append(curr % 10)
                carry = curr // 10

            p1 -= 1
            p2 -= 1

        result.reverse()
        result = [str(i) for i in result]

        return "".join(result)


s = Solution()
print(s.addStrings('6994', '36'))
