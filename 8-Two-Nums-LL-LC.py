# You are given two non-empty linked lists 
# representing two non-negative integers.
# The digits are stored in reverse order
# and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain
# any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

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
        ans_node = node = ListNode(0)
        while(l1 and l2):
            node.val = node.val + l1.val + l2.val
            if node.val > 9:
                node.next = ListNode(1)
                node.val = node.val - 10
            else:
                node.next = ListNode(0) if l1.next or l2.next else None
            node = node.next
            l1 = l1.next
            l2 = l2.next

        return ans_node
            