class Solution1:
    def hammingWeight(self, n: int) -> int:
        """
        Time O(1)   worse case 32-bit integer but still constant
        Space O(1)
        位运算的技巧，n & (n - 1) 会消除当前n的二进制表达式的最后一个1，所以我们要计算有多少个1，
        可以用一个循环不停地消除 1 同时计数，直到 n 变成 0 为止。
        """
        res = 0
        while n:
            # 一直消除1，然后更新n
            n = n & (n - 1)
            # 消除一个1就可以计数一次
            res += 1

        return res


class Solution2(object):
    def hammingWeight(self, n):
        """
        Time O(1)
        Space O(1)
        直接用build-in的function，转化成2进制后计直接count多少个1
        """
        return bin(n).count('1')


s = Solution1()
print(s.hammingWeight(n=11))
print(s.hammingWeight(n=128))
print(s.hammingWeight(n=2147483645))
