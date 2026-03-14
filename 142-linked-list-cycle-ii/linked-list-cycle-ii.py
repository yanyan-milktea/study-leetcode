# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
				    
        slow = fast = head

        # 1. check if cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # 2. find entry
                entry = head
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry

        return None