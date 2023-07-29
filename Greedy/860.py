from typing import List


class Solution:
    def lemonadeChange1(self, bills: [int]) -> bool:
        """
        有如下三种情况：
            情况一：账单是5，直接收下。
            情况二：账单是10，消耗一个5，增加一个10
            情况三：账单是20，优先消耗一个10和一个5，如果不够，再消耗三个5
        局部最优：遇到账单20，优先消耗美元10，完成本次找零。全局最优：完成全部账单的找零。
        """
        five, ten, twenty = 0, 0, 0

        for i in bills:
            if i == 5:
                five += 1

            if i == 10:
                if five <= 0:
                    return False

                ten += 1
                five -= 1

            if i == 20:
                # 优先消耗10美元，因为5美元的找零用处更大，能多留着就多留着
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                    twenty += 1
                elif five >= 3:
                    five -= 3
                    twenty += 1
                else:
                    return False

        return True

    def lemonadeChange2(self, bills: List[int]) -> bool:
        """
        另一种写法，通过找零来判断是否有bill
        """
        five, ten, twenty = 0, 0, 0
        for bill in bills:
            charge = bill - 5
            if charge == 0:
                five += 1
            elif charge == 5:
                ten += 1
                if five <= 0:
                    return False
                else:
                    five -= 1
            elif charge == 15:
                twenty += 1
                if ten >= 1:
                    ten -= 1
                    if five >= 1:
                        five -= 1
                    else:
                        return False
                else:
                    if five >= 3:
                        five -= 3
                    else:
                        return False

        return True


s = Solution()
print(s.lemonadeChange1(bills=[5, 5, 5, 10]))


