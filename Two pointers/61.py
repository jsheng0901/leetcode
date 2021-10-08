# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        获取单链表的倒数第 N + 1 与倒数第 N 个节点
        将倒数第 N + 1 个节点的 next 指向 null
        将链表尾节点的 next 指向 head
        返回倒数第 N 个节点
        注意：假如链表节点长度为 len，
        则右移 K 位与右移动 k % len 的效果是一样的
        就像是长度为 1000 米的环形跑道，
        你跑 1100 米与跑 100 米到达的是同一个地点
        """
        if head:
            p1 = head
            p2 = head
            count = 1
            i = 0
            while i < k:
                if p2.next:
                    count += 1
                    p2 = p2.next
                else:           # 当k大于链表长度的时候，要更新k并且重置p2到head
                    k = k % count
                    i = -1
                    p2 = head
                i += 1

            while p2.next:      # 当p1和p2相差k的时候，同步向后跳就行
                p1 = p1.next
                p2 = p2.next

            if p1.next:
                tmp = p1.next
            else:
                return head
            p1.next = None
            p2.next = head
            return tmp


