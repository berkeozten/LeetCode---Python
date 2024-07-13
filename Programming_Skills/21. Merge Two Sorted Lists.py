# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curNode = ListNode()
        headNode = curNode
        #print(list1, list2)

        while True:
            if list1 and list2:
                curNode.next = ListNode()
                curNode = curNode.next
                if list1.val <= list2.val:
                    curNode.val = list1.val                    
                    list1 = list1.next
                else: 
                    curNode.val = list2.val
                    list2 = list2.next
            elif list1:
                curNode.next = list1
                break
            elif list2:
                curNode.next = list2
                break
            else:
                break


        return headNode.next
        