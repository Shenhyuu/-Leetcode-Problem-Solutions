# Light version

	

# 使用栈解决
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p, s = head, []
        while p:
            s.append(p)
            p = p.next
        p, i = head, len(s) - 1
        while i >= 0:
            if s[i].val != p.val:
                return False
            p, i = p.next, i-1
        return True