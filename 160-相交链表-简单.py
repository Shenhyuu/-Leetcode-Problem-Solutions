# 栈
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s1, s2, p1, p2 = [], [], headA, headB
        while p1:
            s1.append(p1)
            p1 = p1.next
        while p2:
            s2.append(p2)
            p2 = p2.next
        i, j, ans = len(s1) - 1, len(s2) - 1, None
        while i >= 0 and j >= 0 and s1[i] == s2[j]:
            ans = s1[i]
            i, j = i-1, j-1
        return ans


# 集合
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s, p, q = set(), headA, headB
        while p:
            s.add(p)
            p = p.next
        while q:
            if q in s:
                return q
            else:
                q = q.next
        return None