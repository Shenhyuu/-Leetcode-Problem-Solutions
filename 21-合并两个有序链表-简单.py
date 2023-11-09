# Light version:
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = vnode = ListNode(-1)
        while list1 and list2:
            if list1.val <= list2.val:
                p.next, list1 = list1, list1.next
            else:
                p.next, list2 = list2, list2.next
            p = p.next
        p.next = list1 if list1 else list2
        return vnode.next

# Simple version:
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 实例化虚拟节点
        vnode = ListNode(-1)
        # 创建指针
        p = vnode
        # 遍历链表1、2，当链表1、2任一为空结束循环（不进入）
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next
        # 将剩余链表接入新链表尾部，剩余部分非链表1即2
        if list1 is None:
            p.next = list2
        else:
            p.next = list1
        return vnode.next