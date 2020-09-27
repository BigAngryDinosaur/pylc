# @lc app=leetcode id=2 lang=python3

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_list(vec: List[int]) -> ListNode:

    head = ListNode()
    node = head

    for num in vec:
        new_node = ListNode(num)
        node.next = new_node
        node = node.next

    return head.next

def to_vec(head: ListNode) -> List[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        res = ListNode()
        head = res
        carry = 0

        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            s = num1 + num2 + carry
            carry = s // 10
            res.next = ListNode(s % 10)
            res = res.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry:
            res.next = ListNode(carry)

        return head.next
