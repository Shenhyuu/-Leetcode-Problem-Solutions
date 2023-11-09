# 对当前节点，向后寻找到第一个与其值不相同的节点或找到尾节点，然后将前一节点指向该节点，即
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = vhead = ListNode(-1,head)
        if head:
            while slow.next and slow.next.next:
                fast = slow
                while fast.next and fast.val == slow.val:
                    fast = fast.next
                slow.next = fast.next
                slow = slow.next
        return vhead.next
            


# 对于下一个值与下下个值比较，如果相等，下一个 
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = vhead = ListNode(0, head)
        if head:
            while p.next and p.next.next:
                if p.next.val == p.next.next.val:
                    x = p.next.val
                    while p.next and p.next.val == x:
                        p.next = p.next.next
                else:
                    p = p.next
        return vhead.next