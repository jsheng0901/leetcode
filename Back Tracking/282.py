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
                self.result.append("".join(path[1:]))  # 因为最开始永远是+号，所以取index 1 之后的数字
            return

        curr = curr * 10 + int(num[start_index])
        str_curr = str(curr)

        # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
        # valid operand. Hence, this check
        if curr > 0:
            # NO OP recursion
            # 第一种情况：没有任何运算符号操作
            # value，curr和prev都为原来值，因为没有做任何运算也就是思路里面的当前都是digital并且一直continue，没有符合运算
            self.backtracking(num, target, start_index + 1, prev, curr, value, path)

        # 第二种情况：addition
        path.append('+')
        path.append(str_curr)
        # 当前数值传入下一个，因为做了运算，所以是0开始。这里等价于思路一里面，遇到运算符号后，要初始化当前数值
        # value等价于思路一里面stack里面从开始到目前的数值和
        self.backtracking(num, target, start_index + 1, curr, 0, value + curr, path)
        path.pop()
        path.pop()

        # Can subtract or multiply only if there are some previous operands
        if path:
            # 第三种情况：subtraction，当前value为之前的value减去curr值，也就是stack里面入栈-curr，之后sum
            path.append('-')
            path.append(str_curr)
            self.backtracking(num, target, start_index + 1, -curr, 0, value - curr, path)
            path.pop()
            path.pop()

            # 第四种情况：multiplication
            path.append('*')
            path.append(str_curr)
            # 这里的value等价于之前的value减去前一个值，再前一个值乘以当前值，其实就是stack里面弹出栈顶元素和当前元素相乘后，之后sum的操作
            # 只是这里sum提前进行了，所以需要先减去sum过的prev值
            self.backtracking(num, target, start_index + 1, curr * prev, 0, value - prev + (curr * prev), path)
            path.pop()
            path.pop()

        return

    def addOperators(self, num: str, target: int) -> [str]:
        """
        Time O(n × 4^n) 四种插入方法，n个数字，每个组合里面需要join一遍所有元素
        Space O(n)
        拆开四种情况的运算在loop里面，每种情况对应的输入值不一样，这里的path其实就是思路1里面的stack。
        """
        self.backtracking(num, target, 0, 0, 0, 0, [])

        return self.result


s = Solution2()
print(s.addOperators('105', 105))
