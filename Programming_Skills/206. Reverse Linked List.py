class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        front = None
        while cur != None:
            front = cur.next
            cur.next = prev
            prev = cur
            cur = front

        return prev