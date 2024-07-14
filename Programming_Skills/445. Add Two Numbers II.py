# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1 = self.getLength(l1)
        len2 = self.getLength(l2)
        
        if len1 > len2:
            dif = len1 - len2
            for i in range(dif):
                l2 = ListNode(0,l2)
        elif len2 > len1:
            dif = len2 - len1
            for i in range(dif):
                l1 = ListNode(0,l1)

        # Going recursive now
        carier = self.addTwoNodes(l1,l2)

        if carier != 0:
            return ListNode(carier,l1)
        else:
            return l1
            



    def addTwoNodes(self, l1: Optional[ListNode], l2: Optional[ListNode], carier=0) -> int:
        if not l1:
            return 0
        carier = self.addTwoNodes(l1.next,l2.next,carier)
        temp = l1.val + l2.val + carier
        carier = temp // 10
        l1.val = temp % 10
        return carier
        
    def getLength(self, l1: Optional[ListNode]) -> int:
        len1 = 0
        pointer = l1
        while pointer:
            len1 += 1
            pointer = pointer.next
        return len1
