class Solution:
    def removeSpace(self, s):
        new_s = ''
        for i in s:
            if i.isalpha():
                new_s += i.lower()
            elif i.isnumeric():
                new_s += i

        return new_s

    def isPalindrome(self, s: str) -> bool:
        """同时check是否是字符或者数字，如果不是就跳过，是则"""
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