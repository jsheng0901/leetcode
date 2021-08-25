# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        """双指针，三种case insert node"""
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node

        prev, curr = head, head.next

        insert = False

        while True:
            if prev.val <= insertVal <= curr.val:
                # 当前指针大于前一个指针
                insert = True
            elif prev.val > curr.val:
                # 当前指针是最小值，前一个指针是最大值
                if insertVal >= prev.val or insertVal <= curr.val:
                    insert = True

            if insert:
                prev.next = Node(insertVal, curr)
                return head

            prev, curr = curr, curr.next
            # loop完一圈直接结束
            if prev == head:
                break
        # 所有指针的值相等
        prev.next = Node(insertVal, curr)

        return head



