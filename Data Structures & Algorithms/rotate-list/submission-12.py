# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        r,count  = head, 1
        while r.next:
            count+=1
            r=r.next

        k = k%count
        if k == 0:
            return head
        cur = head
        for i in range(count - k - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        r.next = head
        
        return newHead


