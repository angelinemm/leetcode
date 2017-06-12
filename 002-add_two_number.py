# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root_res = ListNode(0)
        res = root_res
        carry = 0
        while True:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            _sum = l1_val + l2_val + carry
            if _sum >= 10:
                _sum = _sum % 10
                carry = 1
            else:
                carry = 0
            res.val = _sum
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if not l1 and not l2:
                break
            res.next = ListNode(0)
            res = res.next
        if carry:
            res.next = ListNode(1)
        return root_res
