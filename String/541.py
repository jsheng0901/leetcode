def reverseString(s: [str]) -> str:
    """
    0(n/2) time, 0(1) space, loop half of string, use two pointers
    """
    j = len(s) - 1
    for i in range(len(s) // 2):
        s[i] = s[j]
        j -= 1

    return s


def reverseStr(s: str, k: int) -> str:
    """
    O(N) time, loop over str but in 2k step and check length then run reverse string function
    """
    s_list = list(s)                    # change to list first, since string is immutable
    for i in range(0, len(s), 2 * k):   # loop string step by 2 * k
        if i + k <= len(s_list):        # check left str length is smaller than 2k and bigger than 1k
            str_to_be_reverse = s_list[i:i + k]
            s_list[i:i + k] = reverseString(str_to_be_reverse)    # use previous problem function to do reverse
        else:
            str_to_be_reverse = s_list[i:]
            s_list[i:] = reverseString(str_to_be_reverse)

    return "".join(s_list)               # concat final list to sting


class Solution:
    def reverse(self, s):
        s = list(s)
        j = len(s) - 1  # left pointer
        for i in range(len(s) // 2):  # loop only half string
            s[i], s[j] = s[j], s[i]  # change position
            j -= 1

        return ''.join(s)

    def reverseStr(self, s: str, k: int) -> str:
        "此方法不可用，因为重新构造result不会记录没有reverse的部分"
        result = ''

        for i in range(0, len(s), 2 * k):

            if len(s) - i < k:
                result += self.reverse(s[i:])
            elif k <= len(s) - i < 2 * k:
                result += self.reverse(s[i:i + k])
            else:
                result += (self.reverse(s[i:i + k]) + s[i + k:i + 2 * k])

        return result

s = Solution()
print(s.reverseStr(s="abcdefg", k=2))
