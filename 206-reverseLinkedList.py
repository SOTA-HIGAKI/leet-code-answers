from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revHead = ListNode()
        
        while head is not None and head.val != None:
            revHead = self.reverse_iteration(head.val, revHead)
            head = head.next

        return revHead.next

    def reverse_iteration(self, headVal: int, revHead: ListNode) -> ListNode:
        temp = ListNode()
        revHead.val = headVal
        temp.next = revHead
        return temp
