# Light version
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            p = head
            while p.next:
                if p.val == p.next.val:
                    p.next = p.next.next
                else:
                    p = p.next
        return head
	

# Simple version
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
		# 若链表只有空节点，直接返回自身
        if head:
			# 创建指针
            p = head
			# 遍历链表，当p为链表末节点前一节点时为最后一次循环
            while p.next:
				# 如果p的值与p的下一节点相同，直接越过下一节点（删去下一节点）
                if p.val == p.next.val:
                    p.next = p.next.next
                else:
                    p = p.next
        return head