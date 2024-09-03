class Solution1:
    def breakPalindrome(self, palindrome: str) -> str:
        """
        Time O(n)
        Space O(1)
        case 1：长度为1，说明一定不可能
        case 2：全都是a，最后一个变成b
        case 3：只有一个不是a，最后一个变成b
        case 4：多余一个不是a，第一个不是a的变成a
        """
        # case 1
        if len(palindrome) == 1:
            return ""

        # 记录第一个不是a的index
        first_a_index = -1
        # 计算总共多少个a
        count_a = 0
        for i, val in enumerate(palindrome):
            if val != "a" and first_a_index == -1:
                first_a_index = i
            if val == "a":
                count_a += 1

        # case 2 + case 3
        if first_a_index == -1 or count_a == len(palindrome) - 1:
            res = palindrome[:-1] + "b"
        # case 4
        else:
            res = palindrome[:first_a_index] + "a" + palindrome[first_a_index + 1:]

        return res


class Solution2:
    def breakPalindrome(self, palindrome: str) -> str:
        """
        Time O(n)
        Space O(1)
        一模一样的思路，只是换一种方式记录。对于前半部分回文，如果有不是a的情况出现，直接换成a，对应case 4，
        如果全都是a，说明对应case 2，case 3。
        """
        # case 1
        if len(palindrome) == 1:
            return ""

        # 检查前半部分即可
        for i in range(len(palindrome) // 2):
            # case 4
            if palindrome[i] != "a":
                res = palindrome[:i] + "a" + palindrome[i + 1:]
                return res

        # case 2 + case 3
        res = palindrome[:-1] + "b"

        return res


s = Solution2()
print(s.breakPalindrome(palindrome="abccba"))
print(s.breakPalindrome(palindrome="a"))
