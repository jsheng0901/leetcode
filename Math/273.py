class Solution:
    def __init__(self):
        # initialize arrays
        self.ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                     "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def dfs(self, n, path):
        # 第一种情况，如果小于20
        if n < 20:
            # 这里有一种情况是余数是0的时候，如果不提前结束，会append进空string，比如 'Twenty' -> 'Twenty '
            if n == 0:
                return
            path.append(self.ones[n])
        # 第二种情况，100以内
        elif n < 100:
            path.append(self.tens[n // 10])
            self.dfs(n % 10, path)
        # 第三种情况，1000以内
        elif n < 1000:
            self.dfs(n // 100, path)
            # 注意中间有个百位
            path.append('Hundred')
            self.dfs(n % 100, path)
        else:
            # 第四种情况，大于1000，进行切割
            for i in range(3, 0, -1):
                if n >= 1000 ** i:
                    self.dfs(n // (1000 ** i), path)
                    path.append(self.thousands[i])
                    self.dfs(n % (1000 ** i), path)
                    break
        return

    def numberToWords(self, num: int) -> str:
        """
        Time O(log(num))
        Space O(log(num))
        基本上是数学题加DFS的思想。详细见注释。
        """
        # 特殊情况
        if num == 0:
            return 'Zero'

        path = []
        self.dfs(num, path)

        # 最终结果连起来
        return ' '.join(path)


s = Solution()
print(s.numberToWords(num=123))
print(s.numberToWords(num=12345))
print(s.numberToWords(num=1234567))
