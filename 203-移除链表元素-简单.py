# Light version
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        p = vhead = ListNode(-1,head)
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return vhead.next
	

# Simple version
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        vhead = ListNode(-1,head)
        p = vhead
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return vhead.next