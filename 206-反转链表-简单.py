# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:  # 如果链表为空，或者只有一个节点
            return head
        ans = ListNode(-1)
        cur = head

        while cur:
            next = cur.next
            cur.next = ans.next
            ans.next = cur
            cur = next
        return ans.next