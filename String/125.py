class Solution1:
    def isPalindrome(self, s: str) -> bool:
        """
        Time O(n)
        Space O(1)
        同时check是否是字符或者数字，如果不是就跳过，是则判断是否相等，不等则返回false，等则继续判断
        """
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        """
        Time O(n)
        Space O(n)
        同上思路逻辑，只是需要额外空间来移除空格和标点符合先。
        """
        # 移除所有标点符号和空格
        s_list = []
        for c in s:
            if c.isalnum():
                s_list.append(c.lower())

        # 转化成新的string
        new_string = "".join(s_list)

        # 双指针判断是否是回文
        left, right = 0, len(new_string) - 1
        while left < right:
            if new_string[left] != new_string[right]:
                return False
            left += 1
            right -= 1

        return True


s = Solution1()
print(s.isPalindrome(s="A man, a plan, a canal: Panama"))
