# @lc app=leetcode id=307 lang=python3

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        nums = [0] + nums
        self.bit = BinaryIndexedTree(nums)

    def update(self, i: int, val: int) -> None:
        self.bit.change(i+1, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.bit.range(i+1, j+1)


class BinaryIndexedTree:

    def __init__(self, values):
        self.values = values
        self.tree = values.copy()
        self.n = len(values)

        for i in range(1, self.n):
            parent = i + lsb(i)
            if parent < self.n:
                self.tree[parent] += self.tree[i]

    def update(self, i, value):
        while i < self.n:
            self.tree[i] += value
            i += lsb(i)

    def change(self, i, value):
        diff = value - self.values[i]
        self.values[i] = value
        self.update(i, diff)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i &= ~lsb(i)
        return s

    def range(self, start, end):
        return self.sum(end) - self.sum(start-1)


def lsb(i: int) -> int: return i & -i
