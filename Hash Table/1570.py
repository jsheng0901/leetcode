class SparseVector:
    def __init__(self, nums: [int]):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n

    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        构建非0的字典，记录对应的index， 然后判断哪一个最短，loop这个字典，并记录同时index不是0的乘积，叠加进result
        O(n) time, O(l) space
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

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)