from collections import defaultdict


class Solution:
    def __init__(self):
        self.index = 0

    def parse_formula(self, formula):
        n = len(formula)
        cur_freq = defaultdict(int)
        cur_atom = ""
        cur_count = ""

        while self.index < n:
            # uppercase letter
            if formula[self.index].isupper():
                # save the previous atom and count
                if cur_atom:
                    if cur_count == "":
                        cur_freq[cur_atom] += 1
                    else:
                        cur_freq[cur_atom] += int(cur_count)

                cur_atom = formula[self.index]
                cur_count = ""
                self.index += 1

            # lowercase letter
            elif formula[self.index].islower():
                cur_atom += formula[self.index]
                self.index += 1

            # digit, concatenate the count
            elif formula[self.index].isdigit():
                cur_count += formula[self.index]
                self.index += 1

            # left parenthesis
            elif formula[self.index] == "(":
                self.index += 1
                nested_map = self.parse_formula(formula)
                for atom in nested_map:
                    cur_freq[atom] += nested_map[atom]

                    # Right Parenthesis
            elif formula[self.index] == ")":
                # save the last atom and count of nested formula
                if cur_atom:
                    if cur_count == "":
                        cur_freq[cur_atom] += 1
                    else:
                        cur_freq[cur_atom] += int(cur_count)

                self.index += 1
                multiplier = ""
                while self.index < n and formula[self.index].isdigit():
                    multiplier += formula[self.index]
                    self.index += 1

                if multiplier:
                    multiplier = int(multiplier)
                    for atom in cur_freq:
                        cur_freq[atom] *= multiplier

                return cur_freq

        # save the last atom and count
        if cur_atom:
            if cur_count == "":
                cur_freq[cur_atom] += 1
            else:
                cur_freq[cur_atom] += int(cur_count)

        return cur_freq

    def countOfAtoms(self, formula: str) -> str:
        """
        Time O(n^2 + n * log(n) + n)
        Space O(n)
        思路很简单，遇到左括号就近递归，遇到右括号结束递归。里面的所有字符情况需要考虑到。利用栈来存储前一个的信息。详细见注释。
        """
        # parse the formula
        final_freq = self.parse_formula(formula)

        # sort the final map
        final_freq = dict(sorted(final_freq.items()))

        # generate the answer string
        ans = ""
        for atom in final_freq:
            ans += atom
            if final_freq[atom] > 1:
                ans += str(final_freq[atom])

        return ans


s = Solution()
print(s.countOfAtoms(formula="H2O"))
print(s.countOfAtoms(formula="Mg(OH)2"))
print(s.countOfAtoms(formula="K4(ON(SO3)2)2"))
