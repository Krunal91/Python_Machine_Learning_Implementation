# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n = root = ListNode(0)
        if not l1:
            root.next = l2
            return n.next
        if not l2:
            root.next = l1
            return n.next

        while (l1 or l2):
            if l1 and l2:

                if l1.val < l2.val:
                    root.next = l1
                    l1 = l1.next
                else:
                    root.next = l2
                    l2 = l2.next
                root = root.next
                continue
            if l1:
                root.next = l1
                l1 = l1.next
                root = root.next
                continue
            if l2:
                root.next = l2
                l2 = l2.next
                root = root.next

        return n.next
