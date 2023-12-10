from typing import List


class Solution:
    def __init__(self):
        self.res = 0

    def traversal(self, tree_map, depth, position, cur_sum):
        # 如果此节点不存在，说明走到空节点，结束递归
        if (depth, position) not in tree_map:
            return

        # 当前path的sum
        cur_sum += tree_map[(depth, position)]
        # 左孩子节点的坐标
        left = (depth + 1, position * 2 - 1)
        # 右孩子节点的坐标
        right = (depth + 1, position * 2)
        # 如果当前节点是叶子结点，说明走到底了，记录进总和
        if left not in tree_map and right not in tree_map:
            self.res += cur_sum
            
        # 递归左边
        self.traversal(tree_map, left[0], left[1], cur_sum)
        # 递归右边
        self.traversal(tree_map, right[0], right[1], cur_sum)

        return

    def pathSum(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        先构建树，用字典的形式构建，key: (depth, position) value: node value。构建完后前序遍历整棵树，记录path的sum，
        走到底的时候记录路径总和进全局变量。这题最trick的地方是如何构建树，每个节点在树里面depth和position都是unique的，所以可以用词信息
        构建树，每个节点的左右子树节点和父节点的depth和position的关系很巧妙的关系是:
        (depth, position) -> (depth + 1, position * 2) and (depth + 1, position * 2 - 1)
        """
        # 构件树
        tree_map = {}

        for num in nums:
            num_str = str(num)
            depth, position, val = int(num_str[0]), int(num_str[1]), int(num_str[2])
            # 坐标为key，value为值
            tree_map[(depth, position)] = val

        self.traversal(tree_map, 1, 1, 0)

        return self.res


s = Solution()
print(s.pathSum(nums=[111, 217, 221, 315, 415]))
