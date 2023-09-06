class Solution:
    def reverseString1(self, s: [str]) -> str:
        """
        Time O(n/2)
        Space O(1)
        双指针思路，原地循环交换，for loop写法
        """
        end_index = len(s) - 1
        for i in range(len(s) // 2):
            s[i], s[end_index] = s[end_index], s[i]
            end_index -= 1

        return s

    def reverseString2(self, s: [str]) -> str:
        """
        同上，while loop写法
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s


s = Solution()
print(s.reverseString1(["h", "e", "l", "l", "o", "f"]))
