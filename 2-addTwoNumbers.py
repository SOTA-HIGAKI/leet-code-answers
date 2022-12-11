from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        length1 = 0
        length2 = 0
        head1 = l1
        head2 = l2
        while head1 is not None:
            head1 = head1.next
            length1 += 1
        while head2 is not None:
            head2 = head2.next
            length2 += 1

        head1 = l1
        head2 = l2
        head = l1 if length1 >= length2 else l2
        start = head
        overNumber = 0
        for _ in range(max(length1, length2)):
            head1Val = head1.val if head1 else 0
            head2Val = head2.val if head2 else 0
            addedNumber = head1Val + head2Val + overNumber
            if addedNumber >= 10:
                overNumber = 1
                addedNumber -= 10
            else:
                overNumber = 0
            head.val = addedNumber
            if head.next is not None:
                head = head.next
            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None
        if overNumber == 1:
            head.next = ListNode(val=1)
        return start