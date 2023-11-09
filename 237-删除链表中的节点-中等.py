# 删除一个元素，除了可以修改其前一个节点，也可以将后一个节点的值复制到待删除节点，然后删除被复制节点。
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next