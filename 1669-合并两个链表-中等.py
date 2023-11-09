class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        p = q = vhead = ListNode(-1)
        vhead.next = list1
        for i in range(a):
            p, q = p.next, q.next
        for i in range(b-a+1):
            q = q.next
        p.next = list2
        while p.next:
            p = p.next
        p.next = q.next
        return vhead.next