class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Time O(1)
        Space O(1)
        位运算的技巧，一个数如果是2的次方，那么这个数的二进制表达方式一定只含有一个1，用 & 来check是否只含有一个1
        """
        if n <= 0:
            return False

        return (n & (n - 1)) == 0


class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Time O(log(n))
        Space O(1)
        典型的二分法解法，一直除直到等于1
        """
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1


s = Solution1()
print(s.isPowerOfTwo(n=16))
print(s.isPowerOfTwo(n=3))
