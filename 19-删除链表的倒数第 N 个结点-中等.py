# 快慢指针
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = vhead = ListNode(-1, head)
        fast = head
        for i in range(n):
            fast = fast.next
        while fast:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return vhead.next


# 多次遍历
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p, cnt, vhead = head, 0, ListNode(-1,head)
        while p:
            p, cnt = p.next, cnt + 1
        p = vhead
        for i in range(cnt - n):
            p = p.next
        p.next = p.next.next
        return vhead.next


# 栈
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = []
        p = vhead = ListNode(-1,head)
        while p:
            s.append(p)
            p = p.next
        index = - (n+1)
        s[index].next = s[index].next.next
        return vhead.next