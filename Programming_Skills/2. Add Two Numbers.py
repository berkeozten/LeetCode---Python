# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        carier = 0
        prev = ListNode(next=head)

        while l1 and l2:
            temp = l1.val + l2.val + carier
            carier = temp // 10
            l1.val = temp % 10
            prev = prev.next
            l1 = l1.next
            l2 = l2.next
            #print(prev, l1, l2)

        if l1:
            while carier != 0 and l1:
                temp = l1.val + carier
                carier = temp // 10
                l1.val = temp % 10
                if not l1.next and carier != 0:
                    l1.next = ListNode(val = carier)
                    carier = 0
                    break
                else:
                    l1 = l1.next
                    prev = prev.next
        elif l2:
            prev.next = l2
            while carier != 0 and l2:
                temp = l2.val + carier
                carier = temp // 10
                l2.val = temp % 10
                if not l2.next and carier != 0:
                    l2.next = ListNode(val = carier)
                    carier = 0
                    break
                else:
                    l2 = l2.next
                    prev = prev.next

        if carier != 0:
            prev.next = ListNode(val = carier)
            carier = 0

        return head

                    




        

        