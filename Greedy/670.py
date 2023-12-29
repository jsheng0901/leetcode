class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        Time O(9 * n --> n)
        Space O(n)
        greedy, loop num form 9 - 0, if we find digit then we loop through begin,
        when find one number smaller than digit, swap the num and return, if not, keep find next digit.
        从后向前，从9到0开始遍历，找到第一个最大的后面的数字同时前面start的index小于后面这个数字的时候，进行swap。
        """
        num_list = [int(i) for i in str(num)]
        digit = 9
        start = 0

        while digit > 0:
            # 从后向前
            for i in range(len(num_list) - 1, -1, -1):
                # 如果找到一个等于digital的数字说明可以开始找这个数字前第一个小于的数字
                if num_list[i] == digit:
                    # 如果大于等于则start指针继续向前走
                    while num_list[start] >= digit:
                        start += 1
                        # 如果超越界说明digital是最小的数字，前面没有更小的
                        if start >= len(num_list) - 1:
                            return num
                    # 如果大于当前位置，说明此digital不是最小的
                    if start >= i:
                        break
                    # 找到进行swap
                    num_list[start], num_list[i] = num_list[i], num_list[start]
                    # 返回结果
                    return int("".join([str(n) for n in num_list]))
            digit -= 1

        return num


s = Solution()
print(s.maximumSwap(num=2736))
