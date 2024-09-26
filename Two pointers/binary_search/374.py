# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int, pick) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    elif num == pick:
        return 0


class Solution:
    def guessNumber(self, n: int, pick) -> int:
        """
        Time O(log(n))
        Space O(1)
        标准二分法写法，原题目没有guess 和 pick，这里为了test，自己加的。
        """
        left = 0
        right = n

        while left <= right:
            mid = left + (right - left) // 2

            guess_res = guess(mid, pick)

            if guess_res == -1:
                right = mid - 1
            elif guess_res == 1:
                left = mid + 1
            elif guess_res == 0:
                return mid


s = Solution()
print(s.guessNumber(n=10, pick=6))
print(s.guessNumber(n=1, pick=1))
