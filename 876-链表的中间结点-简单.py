# 快慢指针
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        return slow