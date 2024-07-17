class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution():
    def deleteList(self, items, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next:
            if current.next.val in items:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(s.deleteList({3}, head))