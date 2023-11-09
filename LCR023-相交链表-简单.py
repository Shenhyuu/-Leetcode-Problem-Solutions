# 集合法（Hash法）
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        p = headA
        while p:
            s.add(p)
            p = p.next
        p = headB
        while p:
            if p in s:
                return p
            p = p.next
        return None

# 压栈法，麻烦但可以练习栈操作的熟练度
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2, s1, s2 = headA, headB, [], []
        # 对两个链表的节点全部压栈
        while p1:
            s1.append(p1)
            p1 = p1.next
        while p2:
            s2.append(p2)
            p2 = p2.next
        # 由于链表末端是共用的，逆序比对至一个差异项，则差异项的下一个节点即为起始公共节点
        i, j, ans = len(s1) - 1, len(s2) - 1, None
        while i >= 0 and j >= 0 and s1[i] == s2[j]:
            ans, i, j = s1[i], i - 1, j - 1
        return ans