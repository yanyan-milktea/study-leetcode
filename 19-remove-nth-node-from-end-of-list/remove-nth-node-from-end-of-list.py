# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = dummy = ListNode(0)
        dummy.next = head

        # fast moves forward n steps
        for i in range(n):
            fast = fast.next

        while fast.next:
            # fast moves to the end
            fast = fast.next
            # slow moves to n - 1
            slow = slow.next

        # remove nth node from end of list
        slow.next = slow.next.next

        return dummy.next
        