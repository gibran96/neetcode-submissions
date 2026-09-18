# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        node = head
        l = 1
        while head.next:
            l += 1
            head = head.next
        print(l)
        i = 0
        if (l - n) == 0:
            return node.next
        current = node
        while i != (l - n - 1):
            current = current.next
            i += 1
        current.next = current.next.next
        return node
        