from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes = []
        nodes.append(head.val)

        while True:
            if head.next is not None:
                head = head.next
                nodes.append(head.val)
            else:
                break

        while True:
            if len(nodes) <= 1:
                return True
            elif nodes[0] != nodes[-1]:
                return False
            else:
                nodes.pop(0)
                nodes.pop()
