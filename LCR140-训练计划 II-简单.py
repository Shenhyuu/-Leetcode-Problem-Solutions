# 快的先走n步，最后慢的距结束n步
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        fast = slow = head
        while cnt > 0:
            fast, cnt = fast.next, cnt - 1
        while fast:
            fast, slow = fast.next,slow.next
        return slow