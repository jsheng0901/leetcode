# 2024-05-04

# The developers at Amazon employ several algorithms for encrypting passwords. In one algorithm, the developers aim
# to encrypt palindromic passwords. Palindromic passwords are ones that read the same forward and backward.
#
# The algorithm rearranges the characters to have the following characteristics:
#
# It is a rearrangement of the original palindromic password. It is also a palindrome. Among all such palindromic
# rearrangements, it is the lexicographically smallest. Given the original palindromic password that consists of
# lowercase English characters only, find the lexicographically smallest palindrome.
#
# A string s is considered to be lexicographically smaller than the string t of the same length if the first
# character in s that differs from that in t is smaller. For example, "abcd" is lexicographically smaller than "abdc"
# but larger than "abad"
#
# Note that the encrypted password might be the same as the original password if it is already lexicographically
# smallest.
#
# Function Description
#
# Complete the function findEncryptedPassword in the editor.
#
# findEncryptedPassword has the following parameter:
#
# string password: the original palindromic password
# Returns
#
# string: the encrypted password


class Solution:
    def findEncryptedPassword(self, password: str) -> str:
        """
        Time O(n)
        Space O(1)
        对一个回文构建另一个首字母最小的回文。先构建一个数组存储所有字母出现的顺序。
        然后从最小的字母开始遍历，如果出现就判断是奇数还是偶数，奇数的话，中间位置就是当前字母，剩下的出现次数平均分配到左右两侧。
        最后全部连接起来即可。
        """
        # 构建数组存储出现频率
        freq = [0] * 26
        for c in password:
            idx = ord(c) - 97
            freq[idx] += 1

        left = ""
        right = ""
        mid = ""
        # 一个一个字母遍历
        for i in range(26):
            # 没有出现过直接跳过
            if freq[i] == 0:
                continue
            # 奇数次，中间值就是次字母
            if freq[i] % 2 != 0:
                mid = chr(i + 97)
                freq[i] -= 1
            # 两边出现的形式
            pattern = (freq[i] // 2) * chr(i + 97)
            # 分别加入进去
            left += pattern
            right = pattern + right

        # 连接起来三个部分
        return left + mid + right


s = Solution()
print(s.findEncryptedPassword(password="babab"))
print(s.findEncryptedPassword(password="yxxy"))
print(s.findEncryptedPassword(password="ded"))
