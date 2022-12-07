# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

            # 1, 2n でも 1, 2n+1 でも middleはn+1 なのでfastには2n+1まで進んでほしいですね。この条件式だと 2n-1 まで来た時に 2n+1 あると止まらない
            # したがって 2n：偶数の場合はもう一個すすめる必要がありますね
        if fast.next is not None:
            return slow.next
        return slow

# memo
# fast and slow method(two-pointer)