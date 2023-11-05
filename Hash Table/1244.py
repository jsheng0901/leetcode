from sortedcontainers import SortedDict


class Leaderboard1:

    def __init__(self):
        """
        Time O(1)
        Space O(n)
        初始化一个字典存储id -> score 的关系，和一个单调递减栈，第一个数字为最大分数，
        每个元素需要存储两个信息，(id, score)。
        """
        self.id_to_score = {}
        self.scores = []

    def addScore(self, playerId: int, score: int) -> None:
        """
        Time O(n)
        Space O(n)
        先检查是否存在，存在则先删除掉记录，注意一定要删除字典和栈内对应的位置元素。之后再正常添加元素，字典添加id和score，
        单调栈查找到相对应的位置，然后直接插入。
        """
        # 检查是否存在过，存在则删除之前记录
        if playerId in self.id_to_score:
            # 这里要注意的是，题目说的是如果存在则更新叠加之前的score，所以先拿出来之前的score然后 + 上新的score
            score += self.id_to_score[playerId]
            # 删除之前的记录
            self.reset(playerId)

        # 添加新的记录，新的score
        self.id_to_score[playerId] = score

        # 如果不是空栈
        if self.scores:
            # 从栈顶向栈底遍历，找到当前大于score的最小值的index
            i = len(self.scores) - 1
            while i >= 0 and self.scores[i][1] < score:
                i -= 1
            # 插入到相对应的位置，栈内元素存储两个信息(id, score) 存储id的目的是为了方便删除用，因为可能会有相等的score但是是不同id的人
            self.scores.insert(i + 1, (playerId, score))
        # 如果是空栈，直接入栈
        else:
            self.scores.append((playerId, score))

        return

    def top(self, K: int) -> int:
        """
        Time O(1)
        Space O(k)
        栈底前k个就是我们要的值，直接loop叠加
        """
        # loop叠加前k个值
        sum_top = 0
        for i in range(K):
            sum_top += self.scores[i][1]

        return sum_top

    def reset(self, playerId: int) -> None:
        """
        Time O(n)
        Space O(n)
        loop一遍栈，找到要删除的id对应的分数，删除栈内元素先，再删除字典，因为要用字典去get此id对应的分数。
        """
        for i in range(len(self.scores)):
            score = self.scores[i]
            # 如果当前分数和id都是对应要删除，则del
            if score[0] == playerId and score[1] == self.id_to_score[playerId]:
                del self.scores[i]
                break
        # 继续删除字典记录
        del self.id_to_score[playerId]


class Leaderboard2:

    def __init__(self):
        """
        Space O(n)
        """
        self.scores = {}
        self.sorted_scores = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:
        """
        Time O(log(n))
        核心思想和第一个是一样的，区别在于第一个方法用stack来存储单调栈，loop搜索需要O(n)的时间，
        而用SortedDict则相当于用一个BST来存储顺序，每次搜索的时候会加快速度从O(n) -> O(log(n))，
        并且这里用inorder顺序搜索BST，自动保证从大到小，注意这里存储的时候用取的是负数，所以是从大到小。
        """
        # The scores dictionary simply contains the mapping from the
        # playerId to their score. The sortedScores contain a BST with
        # key as the score and value as the number of players that have
        # that score.
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sorted_scores[-score] = self.sorted_scores.get(-score, 0) + 1
        else:
            pre_score = self.scores[playerId]
            val = self.sorted_scores.get(-pre_score)
            if val == 1:
                del self.sorted_scores[-pre_score]
            else:
                self.sorted_scores[-pre_score] = val - 1

            new_score = pre_score + score
            self.scores[playerId] = new_score
            self.sorted_scores[-new_score] = self.sorted_scores.get(-new_score, 0) + 1

    def top(self, K: int) -> int:
        """
        Time O(k)
        """
        count, total = 0, 0

        for key, value in self.sorted_scores.items():
            times = self.sorted_scores.get(key)
            for _ in range(times):
                total += -key
                count += 1

                # Found top-K scores, break.
                if count == K:
                    break

            # Found top-K scores, break.
            if count == K:
                break

        return total

    def reset(self, playerId: int) -> None:
        """
        Time O(log(n))
        在sorted_scores这个BST里面找target需要log(n)的时间
        """
        pre_score = self.scores[playerId]
        if self.sorted_scores[-pre_score] == 1:
            del self.sorted_scores[-pre_score]
        else:
            self.sorted_scores[-pre_score] -= 1
        del self.scores[playerId]


# Your Leaderboard object will be instantiated and called as such:
# [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
# [[],[1,13],[2,93],[3,84],[4,6],[5,89],[6,31],[7,7],[8,1],[9,98],[10,42],[5],[1],[2],[3,76],[4,68],[1],[3],[4],[2,70],[2]]
obj = Leaderboard2()
obj.addScore(1, 13)
obj.addScore(2, 93)
obj.addScore(3, 84)
obj.addScore(4, 6)
obj.addScore(5, 89)
obj.addScore(6, 31)
obj.addScore(7, 7)
obj.addScore(8, 1)
obj.addScore(9, 98)
obj.addScore(10, 42)
print(obj.top(5))
obj.reset(1)
obj.reset(2)
obj.addScore(3, 76)
obj.addScore(4, 68)
print(obj.top(1))
obj.reset(3)
obj.reset(4)
obj.addScore(2, 70)
obj.reset(2)
