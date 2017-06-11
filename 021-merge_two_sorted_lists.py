# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        if not l2 or (l1 and l1.val < l2.val):
            root = ListNode(l1.val)
            l1 = l1.next
        else:
            root = ListNode(l2.val)
            l2 = l2.next

        current = root
        while l1 or l2:
            if not l1 or (l2 and l1.val > l2.val):
                current.next = ListNode(l2.val)
                l2 = l2.next
            else:
                current.next = ListNode(l1.val)
                l1 = l1.next
            current = current.next
        return root
