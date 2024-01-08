class Solution1:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        Time O(max(num1, num2))
        Space O(n)
        whole idea is added from back and use carry to remember 进位
        """
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


class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        Time O(max(num1, num2))
        Space O(1)
        同上一模一样的逻辑，但是我们直接用string从前往后添加结果，这样就不不需要用list来记录并且不需要reverse后又join起来。
        """
        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        res = ""

        while p1 >= 0 or p2 >= 0 or carry != 0:
            cur = carry

            if p1 >= 0:
                cur += int(num1[p1])
            if p2 >= 0:
                cur += int(num2[p2])

            if cur <= 9:
                carry = 0
                res = str(cur) + res
            else:
                res = str(cur % 10) + res
                carry = cur // 10

            p1 -= 1
            p2 -= 1

        return res


s = Solution2()
print(s.addStrings('6994', '36'))
