class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        """
        time O(n), space O(n)
        局部最优：遇到strNum[i - 1] > strNum[i]的情况，让strNum[i - 1]--，然后strNum[i]给为9，可以保证这两位变成最大单调递增整数。
        从后向前遍历，从前向后会造成改变之前改过的数值
        例如用一个flag来标记从哪里开始赋值9
        :param N:
        :return:
        """
        n_list = list(str(N))

        # flag是用来记录从哪开始变成9的，因为当最后都是9的时候是最大的数字
        flag = len(n_list)

        for i in range(len(n_list)-1, 0, -1):
            if int(n_list[i-1]) > int(n_list[i]):   # 从后向前遍历，遇到前面的比后面的大的时候就减一
                flag = i
                n_list[i-1] = str(int(n_list[i-1]) - 1)

        for j in range(flag, len(n_list)):          # 更新所有为9的位置
            n_list[j] = '9'

        return int(''.join(n_list))


s = Solution()
print(s.monotoneIncreasingDigits(N=100))




