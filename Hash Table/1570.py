from typing import List


class SparseVector1:
    def __init__(self, nums: [int]):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n

    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        Time O(n)
        Space O(l)
        构建非0的字典，记录对应的index， 然后判断哪一个最短，loop这个字典，并记录同时index不是0的乘积，叠加进result
        """
        result = 0
        # iterate through each non-zero element in this sparse vector
        # update the dot product if the corresponding index has a non-zero value in the other vector
        if len(self.nonzeros.keys()) < len(vec.nonzeros.keys()):
            min_dict = self.nonzeros
            max_dict = vec.nonzeros
        else:
            min_dict = vec.nonzeros
            max_dict = self.nonzeros

        for i, n in min_dict.items():
            if i in max_dict:
                result += n * max_dict[i]
        return result


class SparseVector2:
    def __init__(self, nums: List[int]):
        self.no_zeor_index = set()
        self.index_to_value = {}

        for i, v in enumerate(nums):
            if v != 0:
                self.no_zeor_index.add(i)
                self.index_to_value[i] = v

    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        Time O(n)
        Space O(l) * 2
        构建非0的字典，记录index和value的关系，同时记录非0的index进set，
        我们只需要找到非0的集合的交集即可，然后loop交集的index，叠加进result。这样减少loop的元素个数，更快。
        """
        res = 0
        # 找交集
        intersection_index = self.no_zeor_index.intersection(vec.no_zeor_index)
        # 更新结果
        for index in intersection_index:
            res += self.index_to_value[index] * vec.index_to_value[index]

        return res


class SparseVector3:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs.append([index, value])

    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        Time O(n)
        Space O(l)
        构建非0的index和value的pair，双指针遍历整个list pair，如果index相等的情况下加入result，index不相等移动小的那个。
        当array非常sparse的时候，其实最简单的直接遍历所有元素是最快最省memory的，因为不需要额外空间存储list或者hash map。
        另外一种做法是，当另一个array很sparse的时候，我们可以在长的array里面用 binary search 去找到index。时间复杂度可以降到
        O(l1 + l1 * log(l2))
        """
        result = 0
        p, q = 0, 0

        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                result += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1

        return result


v1 = SparseVector2(nums=[1, 0, 0, 2, 3])
v2 = SparseVector2(nums=[0, 3, 0, 4, 0])
print(v1.dotProduct(v2))
