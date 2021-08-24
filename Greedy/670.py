class Solution:
    def maximumSwap(self, num: int) -> int:
        """greedy, loop num form 9 - 0, if we find digit then we loop through begin,
        when find one number smaller than digit, swap the num and return, if not, keep find next digit
        """
        num_list = [int(i) for i in str(num)]
        digit = 9
        start = 0

        while digit > 0:
            for i in range(len(num_list) - 1, -1, -1):
                if num_list[i] == digit:
                    while num_list[start] >= digit:
                        start += 1
                        if start >= len(num_list) - 1:
                            return num

                    if start >= i:
                        break
                    num_list[start], num_list[i] = num_list[i], num_list[start]
                    return int("".join([str(n) for n in num_list]))
            digit -= 1

        return num


