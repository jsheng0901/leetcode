import copy

class Solution1:
    def __init__(self):
        self.result = []
        self.path = ''

    def check_valid(self, target):
        stack = []
        pre_operation = '+'
        self.path += '+'
        num = 0

        for c in self.path:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == " ":
                continue
            else:
                if pre_operation == '+':
                    stack.append(num)
                elif pre_operation == '-':
                    stack.append(-num)
                elif pre_operation == '*':
                    stack.append(stack.pop() * num)
                pre_operation = c
                num = 0

        self.path = self.path[:-1]
        return sum(stack) == target

    def backtracking(self, num, target, start_index, operators):
        self.path += num[start_index]

        if start_index == len(num) - 1:
            if self.check_valid(target):
                print(self.path)
                self.path_copy = copy.deepcopy(self.path)
                self.path_copy = self.path_copy.replace(' ', '')
                self.result.append(self.path_copy)
            return

        if num[start_index] == str(0):
            operators = '+-*'
        for o in operators:
            self.path += o
            self.backtracking(num, target, start_index + 1, operators)
            self.path = self.path[:-2]

        return

    def addOperators(self, num: str, target: int) -> [str]:

        self.backtracking(num, target, 0, '+-* ')

        return self.result


class Solution2:
    def __init__(self):
        self.result = []

    def backtracking(self, num, target, start_index, prev, curr, value, path):
        # 如果loop到最后一个数字， 同时current为0，没有未计算的数字，check是否等于target
        if start_index == len(num):
            if value == target and curr == 0:
                self.result.append("".join(path[1:]))       # 因为最开始永远是+号，所有
            return

        curr = curr * 10 + int(num[start_index])
        str_curr = str(curr)

        if curr > 0:
            self.backtracking(num, target, start_index + 1, prev, curr, value, path)

        # addition
        path.append('+')
        path.append(str_curr)
        self.backtracking(num, target, start_index + 1, curr, 0, value + curr, path)
        path.pop()
        path.pop()

        if path:
            # subtraction
            path.append('-')
            path.append(str_curr)
            self.backtracking(num, target, start_index + 1, -curr, 0, value - curr, path)
            path.pop()
            path.pop()

            # multiplication
            path.append('*')
            path.append(str_curr)
            self.backtracking(num, target, start_index + 1, curr * prev, 0, value - prev + (curr * prev), path)
            path.pop()
            path.pop()

        return

    def addOperators(self, num: str, target: int) -> [str]:
        """拆开四种情况的运算在loop里面，每种情况对应的输入值不一样"""
        self.backtracking(num, target, 0, 0, 0, 0, [])

        return self.result


s = Solution2()
print(s.addOperators('105', 105))
