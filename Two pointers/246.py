class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        """
        Time O(n)
        Space O(1)
        定义可以旋转的数字和旋转后的数字的映射关系，双指针两边判断即可，只需要判断一遍旋转后是否等于另一边不旋转的情况。
        """
        num_to_rotated = {
            "6": "9",
            "9": "6",
            "8": "8",
            "1": "1",
            "0": "0"
        }

        left = 0
        right = len(num) - 1

        # 注意要包含等于的情况，不然一个数字不会进loop
        while left <= right:
            # 如果是不能旋转的数字，直接返回 false
            if num[right] not in num_to_rotated:
                return False
            # 如果可以旋转但是不相等，直接返回 false
            if num[left] != num_to_rotated[num[right]]:
                return False

            # 双指针往中间跳
            left += 1
            right -= 1

        return True


s = Solution()
print(s.isStrobogrammatic(num="962"))
print(s.isStrobogrammatic(num="69"))
print(s.isStrobogrammatic(num="88"))
print(s.isStrobogrammatic(num="101"))
print(s.isStrobogrammatic(num="7"))
