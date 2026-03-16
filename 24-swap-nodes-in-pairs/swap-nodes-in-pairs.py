# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        curr = dummy

        while curr.next and curr.next.next:
            a = curr.next
            b = curr.next.next

            a.next = b.next
            b.next = a
            curr.next = b

            # a becomes the new end node
            curr = a

        return dummy.next
        '''
            dummy → a → b → c → d

            dummy → b → a → d → c

        '''

        