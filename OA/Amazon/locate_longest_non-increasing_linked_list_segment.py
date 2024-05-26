# 2024-03-01

# Amazon Locate Longest non-increasing linked list segment:
# Find the longest NON-Increasing (e.g.  5 4 4 3) in a linked list, and return the start to only that segment.
# so for example if the linked list is 45443, then just return 5443, (longest segment)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def locateLongestList(self, head: ListNode) -> ListNode:
        p1 = head
        cur_length = 0
        max_length = 0
        start_index = 0
        num_node = 0

        while p1 and p1.next:
            if p1.val >= p1.next.val:
                cur_length += 1
            else:
                if max_length < cur_length:
                    max_length = cur_length
                    start_index = num_node - max_length
                    cur_length = 1

            p1 = p1.next
            num_node += 1

        if max_length < cur_length:
            max_length = cur_length
            start_index = num_node - cur_length

        i = 0
        while head:
            if i == start_index:
                start = head
                while max_length > 0:
                    if max_length == 1:
                        head.next = None
                    else:
                        head = head.next
                    max_length -= 1
                break
            i += 1

        return start


node1 = ListNode(5)
node2 = ListNode(4)
node3 = ListNode(4)
node4 = ListNode(3)
s = Solution()
print(s.locateLongestList(node1).val)
