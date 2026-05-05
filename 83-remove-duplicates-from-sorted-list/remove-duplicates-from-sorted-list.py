# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = []
        curr = head
        prev = None

        while curr:
            if curr.val not in f:
                f.append(curr.val)
                prev = curr
            else:
                prev.next = curr.next

            curr = curr.next

        return head