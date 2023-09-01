class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def isPalindromeList(self, array):
        start = 0
        end = len(array) - 1
        while start < end:
            if array[start] != array[end]:
                return False
            else:
                start += 1
                end -= 1

        return True

    def isPalindrome(self, head: ListNode) -> bool:
        """
        Time O(n)
        Space O(n)
        先转化成数组，然后按照数组正常check回文。
        """
        array = []

        cur = head
        while cur:
            array.append(cur.val)
            cur = cur.next

        return self.isPalindromeList(array)


class Solution2:
    def reverse_list(self, head: ListNode) -> ListNode:
        """
        O(n) time
        0(1) space
        """
        current = head  # start from firs head
        previous = None  # previous head node which is None at first
        while current:  # loop over linked node, when next is None then out
            tmp = current.next  # save current next node as temp node because this will be next current node
            current.next = previous  # point link back to previous node
            previous = current  # move previous to current node, this must move firs then current pointer
            current = tmp  # move current to temp node

        return previous

    def find_mid_node(self, head):
        slow = head
        fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def isPalindrome(self, head: ListNode) -> bool:
        """
        Time O(n)
        Space O(1)
        先找中位数，然后reverse后半部分链表，然后正常顺序check两个部分的链表是否一致。
        """
        mid = self.find_mid_node(head)    # 找到中间节点

        new_head = self.reverse_list(mid.next)   # reverse中间节点后的部分

        p1 = head
        p2 = new_head

        while p2:               # 对比是否一致
            if p2.val != p1.val:
                return False
            else:
                p2 = p2.next
                p1 = p1.next

        return True


class Solution3:
    def __init__(self):
        self.left = ListNode()

    def traversal(self, right):
        if right is None:       # linked Node 就是树结构，采取后序遍历在从后往前处理节点node，并每次向前()返回值
            return True
        res = self.traversal(right.next)
        if res is True:
            res = right.val == self.left.val
            self.left = self.left.next

        return res

    def isPalindrome(self, head: ListNode) -> bool:
        """
        Time O(n)
        Space O(n) recursive stack
        后续遍历从底部开始check，用一个全局指针从头开始check，每次check两头是否相等，返回true/false。
        """
        self.left = head

        return self.traversal(head)


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4
s = Solution3()
print(s.isPalindrome(node1))
