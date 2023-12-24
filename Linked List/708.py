# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        """
        Time O(n)
        Space O(1)
        双指针，三种case insert node
        """
        # 特殊情况，给定的node是空节点
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node

        prev, curr = head, head.next

        insert = False

        while True:
            # 第一种情况，insert在两个指针中间，当前insert值在两个指针节点中间
            if prev.val <= insertVal <= curr.val:
                # 当前指针大于前一个指针
                insert = True
            # 第二种情况，当前insert值在头尾之间
            elif prev.val > curr.val:
                # 当前指针是最小值，前一个指针是最大值，insert 值要么大于最大值，要么小于最小值
                if insertVal >= prev.val or insertVal <= curr.val:
                    insert = True

            if insert:
                prev.next = Node(insertVal, curr)
                return head

            prev, curr = curr, curr.next
            # 如果一直没有找到合理insert的地方，loop完一圈直接结束
            if prev == head:
                break

        # 第三种情况，所有指针的值相等，选择任意指针都一样，直接选择head指针前面insert
        prev.next = Node(insertVal, curr)

        return head


node1 = Node(1)
node2 = Node(3)
node3 = Node(4)
node2.next = node3
node3.next = node1
node1.next = node3
s = Solution()
print(s.insert(node2, 2))
