class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        vals = []
        curr = self
        while curr.next:
            vals.append(curr.val)
            curr = curr.next
        vals.append(curr.val)
        vals.append('NULL')
        return '->'.join(str(v) for v in vals)


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pre_reversed = head
        reversed = None
        post_reversed = None
        prev = None
        curr = head

        pos = 1
        while pos <= n:
            if m <= pos <= n:
                temp = reversed
                reversed = ListNode(curr.val)
                if pos == m:
                    tail_pre_rev = prev # This is where we will link to the reversed section
                    tail_rev = reversed # This is where we will link to the post-reversed section
                reversed.next = temp
                if pos == n:
                    post_reversed = curr.next
            prev = curr
            curr = curr.next
            pos += 1

        print('@')
        print(pre_reversed)
        print('tail pre rev: {}'.format(tail_pre_rev))
        print(reversed)
        print('tail rev: {}'.format(tail_rev))
        print(post_reversed)
        print('@')

        if tail_pre_rev:
            tail_pre_rev.next = reversed
        tail_rev.next = post_reversed

        if tail_pre_rev:
            return head
        else:
            return reversed


def main():
    five = ListNode(5)
    four = ListNode(4)
    three = ListNode(3)
    two = ListNode(2)
    one = ListNode(1)

    four.next = five
    three.next = four
    two.next = three
    one.next = two

    linked_list = one

    print(linked_list)
    print(Solution().reverseBetween(linked_list, 2, 5))


if __name__ == "__main__":
    main()
