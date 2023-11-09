# 快速
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergetwo(list1,list2):
            if not list1:
                return list2
            if not list2:
                return list1
            if list1.val<list2.val:
                head = list1
                list1=list1.next
            else:
                head=list2
                list2=list2.next
            tmp=head
            while list1 and list2:
                if list1.val<list2.val:
                    tmp.next=list1
                    list1=list1.next
                else:
                    tmp.next=list2
                    list2=list2.next
                tmp=tmp.next
            tmp.next=list1 or list2
            return head
        if len(lists)==0:
            return None
        elif len(lists)==1:
            return lists[0]
        while len(lists)>1:
            res=[]
            for i in range(0,len(lists),2):
                if i==len(lists)-1:
                    res.append(mergetwo(lists[i],None))
                else:
                    res.append(mergetwo(lists[i],lists[i+1]))
            lists=res
        return lists[0]

# 简易
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            vhead, p1, p2 =ListNode(-1), list1, list2
            p = vhead
            while p1 and p2:
                if p1.val <= p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
                p = p.next
            if p1:
                p.next = p1
            else:
                p.next = p2
            return vhead.next
        p = None
        if lists:
            p = lists[0]
            if len(lists) >= 2:
                for i in range(1,len(lists)):
                    p = mergeTwoLists(p,lists[i])
        return p