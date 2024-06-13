# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    return graph[a][b] == 1


class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        Time O(n^2)
        Space O(n)
        暴力解法，两层loop嵌套，找到节点入度是 n - 1，出度是0的节点，就是名人，如果不存在说明没有名人。
        """
        # 初始化，入度和出度数组
        in_degree = [0] * n
        out_degree = [0] * n

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                # 如果 i --> j
                if knows(i, j):
                    # j 的入度 + 1
                    in_degree[j] += 1
                    # i 的出度 + 1
                    out_degree[i] += 1

        # 找到入度为 n - 1，出度为 0 的节点
        for i in range(len(in_degree)):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i

        return -1


class Solution2:
    def findCelebrity(self, n: int) -> int:
        """
        Time O(n)
        Space O(n)
        其实我们并不需要遍历所有情况，我们可以利用名人的特性，逐一淘汰不是名人的节点，剩下的那个就可能是名人。
        这里名人只有四种关系，i --> j j --> i，i --> j j -x- i，i -x- j j --> i，i -x- j j -x- i。可以分成两种情况。详细见注释。
        """
        if n == 1:
            return 0

        # 将所有候选人装进队列
        q = []
        for i in range(n):
            q.append(i)

        # 一直排除，直到只剩下一个候选人停止循环
        while len(q) >= 2:
            # 每次取出两个候选人，排除一个
            cand = q.pop(0)
            other = q.pop(0)
            # 对应情况 i --> j j -x- i
            if knows(cand, other) or not knows(other, cand):
                # cand 不可能是名人，排除，让 other 归队
                q.insert(0, other)
            # 对应情况 i -x- j j --> i
            else:
                # other 不可能是名人，排除，让 cand 归队
                q.insert(0, cand)

        # 现在排除得只剩一个候选人，判断他是否真的是名人
        cand = q.pop(0)
        for other in range(n):
            if other == cand:
                continue
            # 保证其他人都认识 cand，且 cand 不认识任何其他人
            if not knows(other, cand) or knows(cand, other):
                return -1

        # cand 是名人
        return cand


class Solution3:
    def findCelebrity(self, n: int) -> int:
        """
        Time O(n)
        Space O(1)
        同思路2，只是我们并不需要一个list来存储所有节点，利用other 和 cand 的交替变化，模拟了之前操作list的过程，避免了使用额外的存储空间。
        """

        # 先假设 cand 是名人
        cand = 0
        for other in range(1, n):
            if not knows(other, cand) or knows(cand, other):
                # cand 不可能是名人，排除
                # 假设 other 是名人
                cand = other
            else:
                # other 不可能是名人，排除
                # 什么都不用做，继续假设 cand 是名人
                pass

        # 现在的 cand 是排除的最后结果，但不能保证一定是名人
        for other in range(n):
            if cand == other:
                continue
            # 需要保证其他人都认识 cand，且 cand 不认识任何其他人
            if not knows(other, cand) or knows(cand, other):
                return -1

        return cand


graph = [[1, 1, 0], [0, 1, 0], [1, 1, 1]]
s = Solution()
print(s.findCelebrity(n=3))
