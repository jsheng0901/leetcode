# 2024-05-04
# You are given a binary string. Find the minimum number of operations required to reverse it. An operation is
# defined as: Remove a character from any index and append it to the end of the string.
#
# Function Description
#
# Complete the function reverseBinaryString in the editor.
#
# reverseBinaryString has the following parameter:
#
# String s: a binary string
# Returns
#
# int: the minimum number of operations required to reverse the binary string


class Solution:
    def reverse_string(self, s):
        reversed_s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            reversed_s[left], reversed_s[right] = reversed_s[right], reversed_s[left]
            left += 1
            right -= 1

        return "".join(reversed_s)

    def reverseBinaryString(self, s: str) -> int:
        """
        Time O(n)
        Space O(n)
        先reverse一下string，然后开始对比reverse后的和原始的string，如果一样说明不需要操作，如果不一样，原始string往前走一步，操作 +1
        """
        # reverse string先
        reversed_s = self.reverse_string(s)

        p1 = 0
        p2 = 0
        res = 0
        # 开始判断
        while p1 < len(s):
            # 如果不一样，说明需要一次操作，原始string往前走一步判断下一个
            if s[p1] != reversed_s[p2]:
                res += 1
                p1 += 1
            # 如果一样，说明不需要操作，都往前走一步
            else:
                p1 += 1
                p2 += 1

        return res


s = Solution()
print(s.reverseBinaryString(s="00110101"))
print(s.reverseBinaryString(s="101"))
print(s.reverseBinaryString(s="0000001"))

