# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """loop p parent first, and add it to set, then loop q parent, if meet in set then return"""
        p_set = set()
        while p:
            p_set.add(p)
            p = p.parent

        while q:
            if q in p_set:
                return q
            q = q.parent

        return None
