class Solution(object):
    def checkPossibility(self, A):
        N = len(A)
        count = 0
        for i in range(1, N):
            if A[i] < A[i - 1]:
                count += 1
                if count > 1:
                    return False
                # [4,2,3]  [4,2,1]   [1,2,1,2]  [1,1,1,] []
                if i >= 2 and A[i] < A[i - 2]:      # 当遇到波峰的时候，此时的数字要变成波峰对应的数字，这样才可以继续比较
                    A[i] = A[i - 1]

        return True
