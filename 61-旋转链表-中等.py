# 先断再拼
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head:
            p, cnt = head, 0
            while p:
                cnt, p = cnt + 1, p.next
            fast, slow, k = head, head, k % cnt
            if  k:
                for i in range(k):
                    fast = fast.next
                while fast.next:
                    fast, slow = fast.next, slow.next
                fast.next = head
                head = slow.next
                slow.next = None
        return head

            
